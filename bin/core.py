# DATES : 4JAN15 , 7JAN15
# CORE : called by dispatcher.py.
# USE : To read JSON object , and perform functions on it .
# FUNCTIONS: getStruct() , readStruct() , tokenizeResponse() , languageMagic()
# Owner : Jaideep Kekre
# Issues: "Sameer put your issues here"# from expert_system import expert_system
# from dispatcher import dispatcher
from Emoji import no
from Emoji import yes
from expert_system import expert_system
from medibot_helper import bcolors
from telegram_interface import create_keyboard


class core(object):
    """one stop shop for all your NLP needs"""

    def __init__(self, arg_user_id, db_connection):
        super(core, self).__init__()
        self.id = arg_user_id
        print bcolors.HEADER + "USER OBJECT CREATED WITH CHAT ID: " + str(self.id) + "\n"

        self.expert = expert_system(self.id, db_connection)

        #self.dispatcher_obj= dispatcher()


    def response(self, user_response):
        # passes contents of argList to console / dispatcher
        # exitPoint
        # expert_object = expert_system.expert_system()
        # expert_object(response_dict)
        response_dict = dict()
        response_dict['chat_id'] = self.id
        print "User Response is" + " " + user_response

        if self.expert.done == 1:
            expert_advice = None
        else:
            expert_advice = self.expert.run_expert(user_response)

        response_list = list()

        if expert_advice is None:
            response_list.append('Hi ! Please click the button below to begin ! ')
            response_dict['response_list'] = response_list
            response_dict['keyboard'] = create_keyboard(['Begin consultation with Doctor SkyNet'])
            return response_dict

        response_list.append(expert_advice['text'])
        response_dict['response_list'] = response_list
        keyboard_data = expert_advice['keyboard']
        keyboard_data.append('Done')
        response_dict['keyboard'] = create_keyboard(keyboard_data)
        return response_dict

    def language_magic(self, arg_list_of_tokens):
        # gets a list of tokens as arg and does magic on them
        # calls response()
        yes_list = ['ho', 'haan', 'haanji', 'HO', 'Ho', u'\U0001f44d', yes]
        no_list = ['nahi', 'Nahi', 'Na', 'na', 'Nope', 'nope', u"\U0001F44E", no]

        if arg_list_of_tokens in yes_list:
            arg_list_of_tokens = 'Yes'
            print bcolors.WARNING + "Yes Translation Used"
            print bcolors.OKBLUE
        elif arg_list_of_tokens in no_list:
            arg_list_of_tokens = 'No'
            print bcolors.WARNING + "No Translation Used"
            print bcolors.OKBLUE

        response_dict = self.response(arg_list_of_tokens)

        return response_dict



    def read_struct(self, arg_dict):
        # parse Dict and extract relevant info
        # calls tokenizeResponse()
        # print argDict
        response_dict = self.language_magic(arg_dict['text'])
        return response_dict

    def get_struct(self, arg_dict):
        # perform checks on Dict
        # entryPoint
        # TODO: Preprocess string - remove extra spaces, capitalize everything, run
        # through spell check library
        response_dict = self.read_struct(arg_dict)
        return response_dict

    def run_core(self, arg_dict):
        response_dict = self.get_struct(arg_dict)
        return response_dict


def tester():
    print("This is a class , don't run this directly")
    sampleOBJ = core(1234567)

    sampleDict = {'chat_id': 1234567, 'text': 'start'}
    sampleOBJ.run_core(sampleDict)

    sampleDict = {'chat_id': 1234567, 'text': 'No'}
    sampleOBJ.run_core(sampleDict)

    sampleDict = {'chat_id': 1234567, 'text': 'No'}
    sampleOBJ.run_core(sampleDict)


if __name__ == '__main__':
    tester()
