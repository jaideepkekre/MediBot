#!usr/bin/python
# Owner :Jaideep Kekre
# _author_ = Jaideep Kekre/Sameer Deshmukh
# _info_   = Connects to database and populates questions

from question_interface import question_interface
from helper import bcolors
import redis

class populate(object):
    """docstring for populate"""

    def __init__(self):
        super(populate, self).__init__()
        self.connection = redis.Redis(
            host='localhost',
            port=6379, 
            password='')
        self._populate_database()

    def _populate_database(self):
        if not self.connection.get('questions'):
            print bcolors.HEADER + "Could not questions. Populating DB now." + bcolors.ENDC
            db = {
                'fever' : {
                    'question' : "Do you have a fever?",
                    'response' : ['Yes', 'No'],
                    'response_type' : 'ruledchar',
                    'linked_questions' : {
                        'question' : "Please measure your fever with a thermometer and tell us your temperature.",
                        'response_type' : ['int', 'float'],
                        'ranged' : True,
                        'range' : [95, 110],
                        'custom_keyboard' : 'numpad'
                    }
                },

                'body_pain' : {
                    'question' : "Do you have body pain?",
                    'response' : ['Yes', 'No'],
                    'response_type' : 'ruledchar',
                    'linked_questions' : {
                        'question' : "Where are you experiencing pain the most?"
                        'response' : ['Head', 'Abdomen', 'Hands', 'Legs'],
                        'response_type' : 'ruledchar',
                        'loop' : True
                        'linked_questions' : {
                            'question' : "Are you still having body pain elsewhere?",
                            'response' : ['Yes', 'No'],
                            'response_type' : 'ruledchar'
                        }
                    }
                }
            }

    """
    Connect with redis and create a list containing top questions and their
    links (links are contained inside question objects).

    A 'top question' refers to a question that is the starting point to gain
    more information about a particular symptom.

    For example, the question that asks 'Do you have a fever?' and then prompts
    the user to tell more about the fever if he answers 'yes' is a top question.
    """
    def poplulate_questions_top(self):
        list_of_questions_top = list()
        q = question_interface()
        q.question = "Do you have a fever ?"
        q.response = ['yes', 'no']
        q.response_type = 'ruledchar'
        q.tag = 'fever'
        list_of_questions_top.append(q)
        q = question_interface()
        q.question = "Do you have body pain ?"
        q.response = ['yes', 'no']
        q.response_type = 'ruledchar'
        q.tag = 'bodypain'
        list_of_questions_top.append(q)

        print list_of_questions_top
        return list_of_questions_top


def test():
    d = populate()
    x = d.poplulate_questions_top()


if __name__ == '__main__':
