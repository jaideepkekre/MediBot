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

  def get_struct(self,argDict):
    #perform checks on Dict
    #entryPoint
    print("Hi from getStruct")
    pass



  def read_struct(self):
    #parse Dict and extract relevant info
    #calls tokenizeResponse()
    print("Hi from readStruct")
    pass


  def tokenize_response(self,argString):
    #tokenizes a string and returns a list of tokens(optional)
    print("Hi from tokenizeResponse")
    pass


  def language_magic(self,argListOFtokens):
    #gets a list of tokens as arg and does magic on them
    #calls response()
    print("Hi from languageMagic")
    pass


  def response(self,argList):
    #passes contents of argList to console / dispatcher
    #exitPoint
    print("Hi from response")
    pass

  def run_core(self,argDict):
    self.get_struct("sample")
    self.read_struct()
    self.tokenize_response("SampleString")
    self.language_magic(['a','b','c'])
    pass



###############################################

def main():
  print("This is a class , don't run this directly")
  sampleOBJ=core("Kekre")
  sampleOBJ.run_core([1,2,3,4])
  

if __name__ == '__main__':
  main()



    
  



