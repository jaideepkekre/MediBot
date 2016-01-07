#!usr/bin/python
#DATES : 4JAN15 , ___?___ 
#DISPATCHER : called by server.py.
#USE : To read DICT object , and assign it to correct core object . 
#FUNCTIONS:  
#Owner : Jaideep Kekre 
#Issues: "Sameer put your issues here"

import core

# @author Sameer Deshmukh / Jaideep Kekre 
class dispatcher():
  """
  class called by a thread that gets a dict and talks to core for 
  further processing.
  """
  def __init__(self, message_params):
    self.message_params = message_params
    
  def is_message_ready(self):
    return True # change this with a method from core that tells if the message is ready
  
  #author : Sameer 
  def create_dict(self):
    # TODO: Change this 
    d = {
      'chat_id' : self.message_params['chat_id'],
      'text' : "THIS IS WHAT YOU SEND ME BRUH :: " + self.message_params['text']
    }

    return d
  
  #@author Jaideep 
  def dispatch_to_core(self):
    messageDict=self.create_dict()
    #do magic to assign all requests from one user to one object
    coreobj=core.core(messageDict['chat_id'])
    coreobj.run_core(messageDict)

  def run_dispatcher(self):
    self.dispatch_to_core()
    pass

def main():
  sampleDict=dict();
  sampleDict={'chat_id':'athavale' ,'text' : 'yo yo yo GTFO!'}
  sampleDispatch=dispatcher(sampleDict)
  sampleDispatch.run_dispatcher()

if __name__ == '__main__':
	main()

