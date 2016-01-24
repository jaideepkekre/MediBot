#!usr/bin/python
# Owner :Jaideep Kekre
# _author_ = Jaideep Kekre
# _info_   = This module contains a Python Script

from question_interface import question_interface


class populate(object):
    """docstring for populate"""

    def __init__(self):
        super(populate, self).__init__()
        # db connection itit here

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
    x = list()
    x = d.poplulate_questions_top()


if __name__ == '__main__':
    test()
