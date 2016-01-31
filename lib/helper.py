#!usr/bin/python
# Owner :Jaideep Kekre
# _author_ = Jaideep Kekre / Sameer Deshmukh
# _info_   = This file contains classes and functions for various helper routines.

class bcolors:
    """Pretty colours for the terminal"""

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class question_interface_helper():
    """
    This class loads questions from data.py into legit question_interface objects.
    """
  
    def __init__(self):
        pass
  
    @classmethod
    def load_data(self):
        from data import question_data
        from question_interface import question_interface
    
        data = question_data()
        top_questions_list = []
    
        for key, value in data.iteritems():
            top = question_interface()
            temp = top
            while True:
                temp.tag             = value.get('tag') or key
                temp.question        = value['question'] # mandatory with #[] and optional 
                temp.response        = value.get('response') # with #get()
                temp.response_type   = value['response_type']
                temp.response_re     = value.get('response_re')
                temp.ranged          = value.get('ranged')
                temp.range           = value.get('range')
                temp.ret             = value.get('ret')
                temp.is_top_level    = value.get('is_top_level')
                temp.loop            = value.get('loop')
                temp.custom_keyboard = value.get('custom_keyboard')

                if value.has_key('linked_questions'):
                    temp.linked_questions = question_interface()
                    temp = temp.linked_questions
                    value = value['linked_questions']
                else:
                    break

            top_questions_list.append(top)

        return top_questions_list



def test():
    d = question_interface_helper.load_data()
    f = None

    for qi in d:
        if qi.question == "Do you have a fever?":
            f = qi

    if f.question == "Do you have a fever?":
        print bcolors.OKGREEN + "PASS" + bcolors.ENDC

    if f.linked_questions.linked_questions.question == "Are you having intermittent fever over time?":
        print bcolors.OKGREEN + "PASS" + bcolors.ENDC

if __name__ == '__main__':
  test()

