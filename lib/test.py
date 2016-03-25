# date : 17 jan 2016
# use  : Mock various classes and objects for automated testing of the bot. For
# now this file only houses test cases.
# author : @v0dro

from dispatcher import dispatcher
from medibot_helper import bcolors

class tester(object):
    """this class is deprecated for now. stay tuned."""

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

import unittest

class TestDBWithScratchPad(unittest.TestCase):
    def setUp(self):
        from scratch_pad import scratch_pad
        from db_store import db

        self.database = db()
        self.scratch = scratch_pad()
        self.database.set_scratch_pad(self.scratch)

    def test_get_next_unanswered_question(self):
        fever = __import__('fever').data()

        question = self.database.get_next_unanswered_question('fever')
        self.assertEqual(question.question, fever['fever_measure']['question'])

        question = self.database.get_next_unanswered_question('fever')
        self.assertEqual(question.question, fever['fever_periodic']['question'])

    def test_get_specific_question(self):
        inner_question = self.database.get_specific_question(['body_pain', 'body_pain_area'])
        body_pain = __import__('body_pain').data()

        self.assertEqual(inner_question.question, 
            body_pain['body_pain_area']['question'])
        self.assertEqual(inner_question.linked_questions.question, \
            body_pain['body_pain_area']['linked_questions']['question'])

        inner_question = self.database.get_specific_question(['body_pain', 'body_pain_area'])

        self.assertEqual(inner_question, None)

if __name__ == '__main__':
    unittest.main()
