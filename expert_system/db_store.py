#!usr/bin/python
# Owner :Jaideep Kekre
# _author_ = Jaideep Kekre/Sameer Deshmukh
# _info_   = Connects to database and populates questions

import redis

from symptom_validity_table import symptom_validity_table


class db(object):

    def __init__(self):
        self.connection = None
        self.scratch_pad = None
        self.connect_redis()
        self.init_data_if_not_present()

    def connect_redis(self):
        self.connection = redis.StrictRedis(
             host='localhost',
             port=6379, 
             password='')

    def init_data_if_not_present(self):
        data = symptom_validity_table().get_dict()
        for key in data:
            data[key] = 0

        if len(self.connection.hgetall('GLOBAL_SYMPTOM_COUNT')) == 0:
            self.connection.hmset('GLOBAL_SYMPTOM_COUNT', data)

        if len(self.connection.hgetall('GLOBAL_USERNAME_CHATID')) == 0:
            self.connection.hmset('GLOBAL_USERNAME_CHATID', {"" : ""})
    
    """
    increase the count of a symptom in global symptom count by 1.
    """
    def increment_global_symptom(self, symptom):
        self.connection.hincrby('GLOBAL_SYMPTOM_COUNT', symptom, 1)

    """
    get the counts of all or specific symptom.
    """

    def get_global_symptom_count(self, symptom='all'):
        if symptom == 'all':
            return self.connection.hgetall('GLOBAL_SYMPTOM_COUNT')
        else:
            return self.connection.hget('GLOBAL_SYMPTOM_COUNT', symptom)

    """
    set basic data for a particular chat id.
    """
    def set_basic_data_for_chat_id(self, chat_id, key, value):
        self.connection.hset(str(chat_id) + ":basic_data", key, value)

    """
    get all or specific basic data for a particular chat id.
    """
    def get_basic_data_for_chat_id(self, chat_id, basic_data):
        user = str(chat_id) + ":basic_data"
        if basic_data == 'all':
            return self.connection.hgetall(user)
        else:
            return self.connection.hget(user, basic_data)

    """
    #jaideep
    set a particular symptom for a given chat id.

    If the user has not yet reported the symptom, it is automatically created
    and set to '1' the first time this method is called with a given chat ID.

    Else, the symptom count will be incremented by 1 for that given chat ID.
    ALSO INCREMENTS THE COUNT GLOBALLY
    """
    def set_symptom_data_for_chat_id(self, chat_id, symptom):
        user = str(chat_id) + ":symptoms"
        count = self.connection.hget(user, symptom)

        if not count:
            self.connection.hset(user, symptom, 1)
        else:
            self.connection.hincrby(user, symptom)

        self.increment_global_symptom(symptom)

    """
    #jaideep
    get a single or all symptom data for specific chat id.

    returns a number if symptom is given, or a dict of all symptoms if nothing.
    """
    def get_symptom_data_for_chat_id(self, chat_id, symptom='all'):
        user = str(chat_id) + ":symptoms"
        if symptom == 'all':
            return self.connection.hgetall(user)
        else:
            return int(self.connection.hget(user, symptom))

    """
    set the username-chat_id pair in the GLOBAL_USERNAME_CHATID hash.

    Should be called only once per chat id.
    """
    def set_username_chat_id_entry(self,username, chat_id):
        self.connection.hset('GLOBAL_USERNAME_CHATID', username, chat_id)


def test():
    from scratch_pad import scratch_pad

    s = scratch_pad()
    d = db()
    d.increment_global_symptom('fever')

    print d.connection.hget('GLOBAL_SYMPTOM_COUNT', 'fever')
    print d.get_global_symptom_count('all')

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