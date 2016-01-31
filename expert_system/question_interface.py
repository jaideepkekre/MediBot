#!usr/bin/python
# Owner :Jaideep Kekre
# _author_ = Jaideep Kekre
# _info_   = Question interface

import re

from helper import bcolors


class question_interface(object):
    """docstring for QuestionInterface"""

    def __init__(self):
        super(question_interface, self).__init__()
        self.tag = None
        self.question = None
        self.response_re = ['reg_exp_1', 'reg_exp_2', None, None]
        self.response = ['response_1', None, None, None]
        self.response_type = ['int', 'bool', 'float', 'randchar', 'ruledchar']
        self.ranged = None
        self.range = ['lower', 'upper']
        self.ret = ['_#ERROR#_', '_#MISMATCH#_', '_#MULTIPLE#_']
        self.is_top_level = 0
        self.custom_keyboard = 0
        self.linked_questions = None
        self.loop = False

    def verify_response(self, check_via_re, check_via_response, response_to_verify):
        flag = [0, 0, 0, 0]
        flag_index = 0
        index = -1
        if (check_via_re == 1):

            for pattern in self.response_re:
                result = re.search(pattern, response_to_verify, re.I)
                # re.I is for case independent matching
                if result:
                    flag[flag_index] = 1
                flag_index = flag_index + 1
                # to track what re matched
        flag_index = 0
        if (check_via_response == 1):

            for expected_response in self.response:
                index = response_to_verify.find(expected_response)
                if (index != -1):
                    flag[flag_index] = 1

                flag_index = flag_index + 1

        error_flag = 0
        found_at = -1
        index = -1
        for index in flag:
            if index == 1 and error_flag == 1:
                print bcolors.FAIL + self.ret[2]
                return self.ret[2]
            if index == 1:
                error_flag = 1
                found_at = flag.index(1)

        if (error_flag == 1 and found_at > -1):
            print  bcolors.OKGREEN + self.response[index]
            return self.response[index]

        if (error_flag == 0):
            print  bcolors.FAIL + self.ret[1]
            return self.ret[1]


def test():
    q = question_interface()
    q.question = "Do you have a fever ?"
    q.response = ['yes', 'no']
    q.response_type = 'ruledchar'

    q.verify_response(0, 1, 'yesyesyes')
    q.verify_response(0, 1, 'yesyesnoyes')
    q.verify_response(0, 1, 'poyesop')
    pass


if __name__ == '__main__':
    test()
