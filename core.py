#DATES : 4JAN15 , ___?___ 
#CORE : called by dispatcher.py.
#USE : To read JSON object , and perform functions on it . 
#FUNCTIONS: getStruct() , readStruct() , tokenizeResponse() , languageMagic() 
#Owner : Jaideep Kekre 
#Issues: "Sameer put your issues here"


class core(object):
  """one stop shop for all your NLP needs"""
  def __init__(self,argUserID):
    super (core, self).__init__()
    self.id = argUserID
    print(self.id)

######################################### 


  def response(self,argList):
    #passes contents of argList to console / dispatcher
    #exitPoint
    print argList
    pass

  def language_magic(self,argListOFtokens):
    #gets a list of tokens as arg and does magic on them
    #calls response()
    self.response(argListOFtokens)

    pass
  def tokenize_response(self,argString):
    #tokenizes a string and returns a list of tokens(optional)
    list_of_tokens=list()
    list_of_tokens = argString.split(" ")
    self.language_magic(list_of_tokens)
    pass

  def read_struct(self,argDict):
    #parse Dict and extract relevant info
    #calls tokenizeResponse()
    #print argDict 
    self.tokenize_response(str(argDict['text']))
    pass

  def get_struct(self,argDict):
    #perform checks on Dict
    #entryPoint
    self.read_struct(argDict) 

    pass

  def run_core(self,argDict):
    self.get_struct(argDict)
    pass





###############################################

def main():
  print("This is a class , don't run this directly")
  sampleOBJ=core("Kekre")
  sampleDict=sampleDict={'chat_id':'athavale' ,'text' : 'yo yo yo GTFO!'}
  sampleOBJ.run_core(sampleDict)
  

if __name__ == '__main__':
  main()



    
  



