# @author Jaideep 
#
# Purpose: The job of the ES is to take the relevant data from the NLP module
# and generate

from DoctorSkyNet import DoctorSkyNet
from question_interface import question_interface


class expert_system:
    """
    The awesome expert system that we gonna create.
    """

    def __init__(self, chat_id, db_connection):
        self.response = None
        self.status = 0
        self.chat_id = chat_id
        self.AI = DoctorSkyNet(chat_id, db_connection)
        self.done = 0
        pass

    def run_expert(self, user_response):
        q_obj = question_interface()
        key = 'Start'
        # print user_response

        valid_keys = ['Start', 'Begin consultation with Doctor SkyNet']
        if self.status == 0:
            if user_response in valid_keys:
                self.status = 1
            else:

                return None

        if self.status == 1: # stage 1 last response from user stays None
            self.status = 2
            q_obj = self.AI.askdoctor()
            returns = dict()
            returns['text'] = q_obj.question
            returns['keyboard'] = q_obj.response
            return returns

        if self.status == 2: # in stage 2 last response from user is passed to AI 
            q_obj = self.AI.askdoctor(user_response)
            if q_obj is None:
                self.status = 3
                returns = dict()
                returns['text'] = 'Your Test is Complete, Please tell the doctor your ID:' + str(self.chat_id)
                returns['keyboard'] = []
                self.done = 1

                return returns

            returns = dict()
            returns['text'] = q_obj.question
            returns['keyboard'] = q_obj.response
            # print "options are:" + str(q_obj.response)
            return returns




def tester():
    print("This is a class , don't run this directly")


if __name__ == '__main__':
    tester()
