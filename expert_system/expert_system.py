# @author Jaideep 
#
# Purpose: The job of the ES is to take the relevant data from the NLP module
# and generate

from DoctorSkyNet import DoctorSkyNet
from telegram_interface import create_keyboard


class expert_system:
    """
    The awesome expert system that we gonna create.
    """

    def __init__(self):
        self.response = None
        self.status = 0
        self.AI = DoctorSkyNet()
        pass



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
            self.status = 1
        if self.status == 1:
            self.status = 2
            self.AI.askdoctor()
            pass
        if self.hunger != -1 and self.question_flag == 1:
            response = self.ask()
            return response

        text = ""

        for token in arg_list_of_tokens:
            text = text + token

        response['text'] = text
        response['keyboard'] = None
        return response


def tester():
    print("This is a class , don't run this directly")


if __name__ == '__main__':
    tester()
