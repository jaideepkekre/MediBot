# date : 17 jan 2016
# use  : Mock various classes and objects for automated testing of the bot. For
# now this file only houses test cases.
# author : @v0dro

from dispatcher import dispatcher


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


class tester(object):
    """defines methods for easy testing"""

    def __init__(self):
        self.creator = dispatcher()
        self.mock_user_dict = {
            'chat_id': 1,
            'text': ""
        }

    def assert_eql(self, expected, actual):
        if expected == actual:
            print bcolors.OKGREEN + "PASS." + bcolors.ENDC
        else:
            print bcolors.FAIL + "FAIL." + bcolors.ENDC

    def user(self, user_message):
        self.mock_user_dict['text'] = user_message
        self.response_list = self.creator.run_dispatcher(self.mock_user_dict)['response_list']

    def bot(self, bot_response):
        if type(bot_response) == list:
            pass
            # TODO: In case of multiple responses.
        else:
            self.assert_eql(bot_response, self.response_list[0])


t = tester()

# A simple conversation between bot and a brand new user.
# user - I have a fever.
# bot  - Please tell us your temperature after measuring it with a thermometer.
# user - 103
# bot  - Alright. Please tell me your age.
# user - 22
# bot  - Which area of Pune do you reside in?
# user - Dhankawadi
# bot  - Are you experiencing joint pains?
# user - yes
# bot  - Are you feeling severe weakness?
# user - yes
# bot  - Does anybody else in your household or neighbours have fever too?
# user - Yes. My mother and sister.

t.user("I have a fever")
t.bot("Please tell your temperature after measuring with a thermometer.")
t.user("103")
t.bot("Alright. What is your age?")
