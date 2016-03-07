#!/usr/bin/python 

"""
author: Jaideep Kekre
"""
'''
Symptom Legend:
'''
fever = 'fever'
body_pain = 'body_pain'
joint_pain = 'joint_pain'
pain_behind_eyes = 'pain_behind_eyes'
rash='rash'
clay_coloured_bowels = 'clay_coloured_bowels'
fatigue = 'fatigue'
yellow_eyes = 'yellow_eyes'

'''
Rating Legend:
'''

CRITICAL = 20
IMPORTANT= 10
OPTIONAL = 5

dengue = {
                fever 	            : CRITICAL,
                body_pain			: IMPORTANT,
                joint_pain		    : IMPORTANT,
                pain_behind_eyes	: OPTIONAL,
                rash				: OPTIONAL,
                'name'				: "dengue"

         }


hepA=	{
                fever 					: IMPORTANT,
                fatigue		 			: CRITICAL,
                joint_pain				: IMPORTANT,
                clay_coloured_bowels	: IMPORTANT,
                yellow_eyes				: OPTIONAL,
                'name'					: "hepA"
         }


diseases_dict = { 
                dengue['name']  :  dengue,
                hepA['name']    :  hepA,

                }

class Disease(object):
    """Loads data from Diease Dicts into a list of dicts"""
    def __init__(self):
        super(Disease, self).__init__()
    def get_disease(self):
        return diseases_dict


