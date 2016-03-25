#!usr/bin/python
# Owner :Jaideep Kekre
# _author_ = Jaideep Kekre / Sameer Deshmukh
# _info_   = This file contains classes and functions for various medibot_helper routines.
# finalist = list()

class bcolors:
    """Pretty colours for the terminal"""

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
            
""" 
a) create a list of the dict's keys and values;
b) return the key with the max value
"""
def keywithmaxval(d):
    v = list(d.values())
    k = list(d.keys())
    if len(v) == 0:
        return None

    return k[v.index(max(v))]