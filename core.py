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

  def getStruct(self,argDict):
    #perform checks on Dict
    #entryPoint
    print("Hi from getStruct")
    pass

  def readStruct(self):
    #parse Dict and extract relevant info
    #calls tokenizeResponse()
    print("Hi from readStruct")
    pass

  def tokenizeResponse(self,argString):
    #tokenizes a string and returns a list of tokens(optional)
    print("Hi from tokenizeResponse")
    pass

  def languageMagic(self,argListOFtokens):
    #gets a list of tokens as arg and does magic on them
    #calls response()
    print("Hi from languageMagic")
    pass
  def response(self,argList):
    #passes contents of argList to console / dispatcher
    #exitPoint
    print("Hi from response")
    pass

def main():
  print("This is a class , don't run this directly")
  sampleOBJ=core("Kekre")
  sampleOBJ.getStruct("sample")
  sampleOBJ.readStruct()
  sampleOBJ.tokenizeResponse("SampleString")
  sampleOBJ.languageMagic(['a','b','c'])

if __name__ == '__main__':
  main()



    
  



