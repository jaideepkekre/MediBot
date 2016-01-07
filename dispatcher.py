#!usr/bin/python
#DATES : 4JAN15 , ___?___ 
#DISPATCHER : called by server.py.
#USE : To read DICT object , and assign it to correct core object . 
#FUNCTIONS:  
#Owner : Jaideep Kekre 
#Issues: "Sameer put your issues here"

import core

# @author Sameer Deshmukh
class dispatcher():
  """
  class called by a thread that gets a dict and talks to core for 
  further processing.
  """
  def __init__(self, message_params):
    self.message_params = message_params
    
  def is_message_ready(self):
    return True # change this with a method from core that tells if the message is ready

  def response(self):
    # TODO: Change this 
    d = {
      'chat_id' : self.message_params['chat_id'],
      'text' : "THIS IS WHAT YOU SEND ME BRUH :: " + self.message_params['text']
    }

    return d

def main():
	coreobj=core.core("kekre")
	coreobj.run_core("")
	pass

if __name__ == '__main__':
	main()

