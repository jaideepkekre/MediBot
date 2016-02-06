#!usr/bin/python
# Owner :Jaideep Kekre
# _author_ = Jaideep Kekre/Sameer Deshmukh
# _info_   = Connects to database and populates questions

from question_interface import question_interface
from helper import bcolors
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
    def get_unanswered_questions(self, tag_list):
        pass



def test():
    from scratch_pad import scratch_pad

    s = scratch_pad()
    d = db()

    d.set_scratch_pad(s)

    if getattr(d, 'scratch_pad') == s:
        print "PASS1"

    l = d.get_unanswered_questions(['fever'])
    if l.size() == 2:
        print "PASS2"

    if l[0].serial == 0:
        print "PASS3"



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