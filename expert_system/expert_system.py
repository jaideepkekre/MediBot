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

    def __init__(self):
        self.response = None
        self.status = 0
        self.AI = DoctorSkyNet()
        self.done = 0
        pass

    def run_expert(self, user_response):
        q_obj = question_interface()
        key = 'Start'
        print user_response

        if key == user_response:
            self.status = 1

        if self.status == 1:
            self.status = 2
            q_obj = self.AI.askdoctor()
            returns = dict()
            returns['text'] = q_obj.question
            returns['keyboard'] = q_obj.response
            return returns

        if self.status == 2:
            q_obj = self.AI.askdoctor(user_response)
            if q_obj == None:
                self.status = 3
                returns = dict()
                returns['text'] = 'Your Test is Complete'
                returns['keyboard'] = ""
                self.done = 1

                return returns

            returns = dict()
            returns['text'] = q_obj.question
            returns['keyboard'] = q_obj.response
            print "options are:" + str(q_obj.response)
            return returns




def tester():
    print("This is a class , don't run this directly")


if __name__ == '__main__':
    tester()
