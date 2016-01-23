#DATES : 4JAN15 , 7JAN15 
#CORE : called by dispatcher.py.
#USE : To read JSON object , and perform functions on it . 
#FUNCTIONS: getStruct() , readStruct() , tokenizeResponse() , languageMagic() 
#Owner : Jaideep Kekre 
#Issues: "Sameer put your issues here"
# from expert_system import expert_system

import nltk 

class core(object):
  """one stop shop for all your NLP needs"""
  def __init__(self,arg_user_id):
    super (core, self).__init__()
    self.id = arg_user_id
    print("USER OBJECT CREATED WITH CHAT ID: " + str(self.id))

######################################### 


  def response(self,arg_list_of_tokens):
    #passes contents of argList to console / dispatcher
    #exitPoint
    # expert_object = expert_system.expert_system()
    # expert_object(response_dict)
    response_dict                  = dict()
    response_dict['chat_id']       = self.id
    response_dict['response_list'] = arg_list_of_tokens

    return response_dict
    

  def language_magic(self,arg_list_of_tokens):
    #gets a list of tokens as arg and does magic on them
    #calls response()
    response_dict = self.response(arg_list_of_tokens)

    return response_dict

  def tokenize_response(self,arg_string):
    #tokenizes a string and returns a list of tokens(optional)
    list_of_tokens = list()
    list_of_tokens = arg_string.split(" ")
    #add list of tokens to response dict
    response_dict  = self.language_magic(list_of_tokens)
    return response_dict

  def read_struct(self,arg_dict):
    #parse Dict and extract relevant info
    #calls tokenizeResponse()
    #print argDict 
    response_dict = self.tokenize_response(str(arg_dict['text']))
    return response_dict

  def get_struct(self,arg_dict):
    #perform checks on Dict
    #entryPoint
    # TODO: Preprocess string - remove extra spaces, capitalize everything, run 
    # through spell check library
    response_dict = self.read_struct(arg_dict) 
    return response_dict

  def run_core(self,arg_dict):
    response_dict = self.get_struct(arg_dict)
    return response_dict

###############################################

def tester():
  print("This is a class , don't run this directly")
  sampleOBJ  = core(1234567)
  sampleDict = {'chat_id':1234567 ,'text' : 'yo yo yo GTFO!'}
  sampleOBJ.run_core(sampleDict)
  

if __name__ == '__main__':
  tester()



    
  



