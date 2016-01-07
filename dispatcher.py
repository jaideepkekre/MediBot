#!usr/bin/python
#DATES : 4JAN15 , ___?___ 
#DISPATCHER : called by server.py.
#USE : To read DICT object , and assign it to correct core object . 
#FUNCTIONS:  
#Owner : Jaideep Kekre 
#Issues: "Sameer put your issues here"

import core

class dispatcher(object):
    """docstring for dispatcher"""
    def __init__(self, arg):
        super(dispatcher, self).__init__()
        self.arg = arg
    def accept_dict(argDict):
        #sameer : write code to print your dict
        pass

    def dispatch_dict(argDict):
        #
        pass
        

def main():
	
    coreobj=core.core("kekre")
	coreobj.run_core("")
	pass

if __name__ == '__main__':
	main()

