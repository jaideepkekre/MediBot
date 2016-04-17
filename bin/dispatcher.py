#!usr/bin/python
# DATES : 4JAN15 , 7JAN15
# DISPATCHER : called by server.py.
# USE : To read DICT object , and assign it to correct core object .
# FUNCTIONS:
# Owner : Jaideep Kekre
# Issues: "Sameer put your issues here"


import core
from db_store import db
from medibot_helper import bcolors
from telegram_interface import create_keyboard


# @author Sameer Deshmukh / Jaideep Kekre 
class dispatcher():
    """
    class called by a thread that gets a dict and talks to core for
    further processing.
    """

    def __init__(self):
        # dict to store active objects and map them to users
        self.object_list = dict()
        # redis db connection object for the conversation. Pass this to whatever
        # class needs a connection to the db.
        self.db_connection = db()

    def dispatch_to_core(self, arg_dict):
        messageDict = arg_dict
        # dispatching logic goes here
        message = messageDict['text']
        chat_id = messageDict['chat_id']
        Check = self.verify_remove_user(chat_id, message)
        # if check is true , the user object was removed on user "Done"
        if Check == True:
            response_dict = dict()
            response_dict['chat_id'] = chat_id
            response_dict['response_list'] = ["Hi Welcome to MediBot"]
            response_dict['keyboard'] = create_keyboard(['Begin consultation with Doctor SkyNet'])
            return response_dict

        for user in self.object_list:

            if (user == messageDict['chat_id']):
                # print "\n\n\n" + str(user) + " found! , reusing object\n"
                core_obj = self.object_list[user]
                response_dict = core_obj.run_core(messageDict)
                return response_dict

        print bcolors.FAIL + "User with chat id" + str(chat_id) + " not found , creating new object "
        coreobj = core.core(chat_id, self.db_connection)
        self.object_list[chat_id] = coreobj
        # stores created object in class variable for future use.
        response_dict = coreobj.run_core(messageDict)
        return response_dict

    def run_dispatcher(self, arg_dict):
        # called by server()
        # scaffolding code
        # make the initial entry in DB that a username with corresponding chat id
        #   has arrived.
        self.db_connection.set_username_chat_id_entry(
            arg_dict['username'], arg_dict['chat_id'])
        response_dict = self.dispatch_to_core(arg_dict)
        # returned to server()
        # response dict has field 'chat_id' 'response_list'
        # logging
        print bcolors.OKGREEN + "input is :" + (arg_dict['text'])
        print bcolors.OKBLUE + "response is :" + (response_dict['response_list'][0]) + "\n"
        # print self.object_list
        return response_dict

    '''
    if user input is Done , remove user object
    '''

    def verify_remove_user(self, chatid, message):
        if message in ['done', 'Done', 'Exit', 'exit']:
            if chatid in self.object_list.keys():
                self.object_list.pop(chatid)
                print bcolors.FAIL + "Chat ID : " + str(chatid) + " removed"
                # send mail here
                return True
        else:
            return False


def tester():
    sampleDict = dict();
    sampleDict = {'chat_id': 1234, 'text': 'yo yo yo GTFO!'}
    sampleDispatch = dispatcher()
    sampleDispatch.run_dispatcher(sampleDict)
    sampleDispatch.run_dispatcher(sampleDict)
    sampleDict = {'chat_id': 4321, 'text': 'yo yo yo GTFO!'}
    sampleDispatch.run_dispatcher(sampleDict)
    sampleDispatch.run_dispatcher(sampleDict)


if __name__ == '__main__':
    tester()
