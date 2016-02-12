#!usr/bin/python
# Owner :Jaideep Kekre
# _author_ = Jaideep Kekre/Sameer Deshmukh
# _info_   = Connects to database and populates questions

from question_interface import question_interface
from helper import bcolors
from expert_system_helper import question_interface_helper
from scratch_pad import scratch_pad
import redis

class db(object):

    def __init__(self):
        self.connection = None
        self.scratch_pad = None

    def connect_redis(self):
        self.connection = redis.Redis(
            host='localhost',
            port=6379, 
            password='')

    """
    Get redis connection object.

    Must call connect_redis() before invoking this method.
    """
    def redis_connection(self):
        return self.connection

    """
    Set the scratch pad to a scratch_pad() object.
    """
    def set_scratch_pad(self, s):
        if str(s.__class__) != 'scratch_pad.scratch_pad':
            raise(TypeError("You must pass a scratch_pad object."))

        self.scratch_pad = s


    """
    Get a list of question_interface() elements that contain the questions within
    the top level tags that have not yet been answered yet.

    The tag_list should contain only top level tags. All the unanswered questions
    under those tags will be returned in a list.
    """
    def get_next_unanswered_question(self, tag):
        pending_question_tags = self.scratch_pad.query(tag)
        if len(pending_question_tags) == 0:
            return None

        last_unanswered_tag = pending_question_tags[0]
        self.scratch_pad.pop(tag)
        return question_interface_helper.load_linked_questions(
            tag, last_unanswered_tag)[0]


    """
    Get a specific question from the database given the hierarchy if it has 
    NOT BEEN ANSWERED already.

    Return None otherwise.
    """
    def get_specific_question(self, tag_hierarchy):
        if self.scratch_pad.query(tag_hierarchy[1]) == None:
            self.scratch_pad.pop_specific(tag_hierarchy)
            return question_interface_helper.load_linked_questions(
                tag_hierarchy[0], tag_hierarchy[1])[0]

        return None

def test():
    from scratch_pad import scratch_pad

    s = scratch_pad()
    d = db()

    d.set_scratch_pad(s)

    if getattr(d, 'scratch_pad') == s:
        print "PASS1"

    l = d.get_next_unanswered_question('fever')
    if l.question == "Please measure your fever with a thermometer and tell us your temperature.":
        print "PASS2"

    if l.serial == 0:
        print "PASS3"

    q = d.get_specific_question(['body_pain', 'body_pain_area'])

    print q

    # run integration tests in test.py for full testing.


if __name__ == '__main__':
    test()
# notes:
# dengue symptoms:
#   severe headache
#   fever > 101
#   rash
#   muscle pain
#   severe pain behind the eyes
#   joint pain
#   mild bleeding

# malaria symptoms:
#   attacks of chills
#   periodic high fever (upto 104)
#   headache
#   body ache

# hepatitis A:
# indications:
#   had dirty food or water in the past
# symptoms:
#   fever
#   fatigue
#   loss of apetite
#   nausea (elaborate)
#   vomiting
#   abdominal pain
#   clay-coloured bowels
#   joint pain
#   yellowing of eyes