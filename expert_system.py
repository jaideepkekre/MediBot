# @author Sameer
#ToDo
#Owner:Sameer
# call the OBO database and create an understandable JSON format that will
# be understood by the expert system.

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
