#!usr/bin/python
#Owner :Jaideep Kekre
#_author_ = Jaideep Kekre
#_info_   = This module contains a Python Script 

from q_interface import QuestionInterface 

class populate(object):
	"""docstring for populate"""
	def __init__(self):
		super(populate, self).__init__()
		#db connection itit here 

	def poplulate_questions_top():
	
	q=QuestionInterface()
	q.question = "Do you have a fever ?"
	q.response=['yes','no']
	q.response_type='ruledchar'

	list_of_questions_top=list()
	list_of_questions_top.append(q)

	return list_of_questions_top 


		