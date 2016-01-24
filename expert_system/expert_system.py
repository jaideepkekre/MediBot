# @author Jaideep 
#
# Purpose: The job of the ES is to take the relevant data from the NLP module
# and generate  
from random import randint

from db_store import populate
from question_interface import question_interface
from telegram_interface import create_keyboard


class expert_system:
    """
    The awesome expert system that we gonna create.
    """

    def __init__(self):
        self.db_object = populate()
        self.top_questions = list()
        self.top_questions_asked = list()
        self.question = question_interface()
        self.last_question_asked_tag = None
        self.question_flag = 0
        self.call_db()
        self.hunger = 10
        pass

    def call_db(self):
        self.top_questions = self.db_object.poplulate_questions_top()
        self.top_questions_asked = [0] * len(self.top_questions)
        pass

    def return_question(self, symptom):
        if 0 not in self.top_questions_asked:
            self.hunger = -1

            return -1

        index = len(self.top_questions)
        random_index = randint(0, index - 1)

        while self.top_questions_asked[random_index] == 1:
            random_index = randint(0, index - 1)

        self.top_questions_asked[random_index] = 1
        # print self.top_questions
        # print self.top_questions_asked
        # print random_index
        question = self.top_questions[random_index]

        return question

    def ask(self):
        question_object = self.return_question(0)
        response = dict()

        if question_object == -1:
            response['text'] = "Done"
            response['keyboard'] = None
            return response

            # print type (question_object)
        text = question_object.question
        responses = question_object.response
        keyboard = create_keyboard(responses)

        response['text'] = text
        response['keyboard'] = keyboard

        self.last_question_asked_tag = question_object.tag
        self.question_flag = 1

        return response

    def run_expert(self, arg_list_of_tokens):
        response = dict()
        key = '9960'
        if key in arg_list_of_tokens:
            response = self.ask()
            return response

        if self.hunger != -1 and self.question_flag == 1:
            response = self.ask()
            return response

        text = ""

        for token in arg_list_of_tokens:
            text = text + token

        response['text'] = text
        response['keyboard'] = None
        return response

        ###############################################


def tester():
    print("This is a class , don't run this directly")


if __name__ == '__main__':
    tester()
