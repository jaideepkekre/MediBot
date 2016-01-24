# @author Sameer
#
# Purpose: The job of the ES is to take the relevant data from the NLP module
# and generate  
from knowledge_store import knowledge_store

class expert_system()
  """
  The awesome expert system that we gonna create.
  """

  def __init__(self):
    pass

  def call_db(self, arg_dict):
    knowledge = knowledge_store.knowledge_store()
    knowledge.run_knowledge_store(arg_dict)
    pass
  def question(self,arg_dict):
    
    pass 

###############################################

def tester():
  print("This is a class , don't run this directly")


if __name__ == '__main__':
  tester()
