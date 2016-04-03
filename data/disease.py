#!/usr/bin/python 

"""
author: Jaideep Kekre
"""
'''
Symptom Legend:
'''
fever = 'fever'

body_pain = 'body_pain'
body_pain_chest = 'body_pain_chest'
body_pain_head = 'body_pain_head'
body_pain_stomach = 'body_pain_stomach'
body_pain_muscles = 'body_pain_muscles'

joint_pain = 'joint_pain'
pain_behind_eyes = 'pain_behind_eyes'
rash='rash'
clay_coloured_bowels = 'clay_coloured_bowels'
fatigue = 'fatigue'
yellow_eyes = 'yellow_eyes'

fever_periodic = 'fever_periodic'
body_chills = 'body_chills'
head_ache = 'head_ache'

diarrhea = 'diarrhea'
consumed_contaminated_stuff = 'consumed_contaminated_stuff'
extreme_weakness = 'extreme_weakness'
rose_spots = 'rose_spots'

yellow_nails = 'yellow_nails'
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
    body_pain_muscles: OPTIONAL,
    'name'				: "dengue"
}

hepA =	{
    fever 					: IMPORTANT,
    fatigue		 			: CRITICAL,
    joint_pain				: IMPORTANT,
    clay_coloured_bowels	: IMPORTANT,
    yellow_eyes				: OPTIONAL,
    'name'					: "hepA"
}

malaria = {
    fever  : CRITICAL,
    fever_periodic : CRITICAL,
    body_chills : CRITICAL,
    head_ache : OPTIONAL,
    body_pain : OPTIONAL,
    'name' : 'malaria'
}

typhoid_fever = {
    consumed_contaminated_stuff : IMPORTANT,
    fever : CRITICAL,
    diarrhea : IMPORTANT,
    extreme_weakness : IMPORTANT,
    head_ache : IMPORTANT,
    rash : OPTIONAL,
    rose_spots : OPTIONAL,
    'name' : 'typhoid_fever'
}

leptospirosis = {
    consumed_contaminated_stuff : IMPORTANT,
    yellow_eyes : CRITICAL,
    yellow_nails : CRITICAL,
    fever : CRITICAL,
    body_chills : IMPORTANT,
    body_pain : OPTIONAL,
    body_pain_muscles : OPTIONAL,
    'name' : 'leptospirosis'
}

diseases_dict = { 
    dengue['name'] :  dengue,
    hepA['name']   :  hepA,
    malaria['name'] : malaria,
    typhoid_fever['name'] : typhoid_fever,
    leptospirosis['name'] : leptospirosis,
}

class Disease(object):
    """Loads data from Diease Dicts into a list of dicts"""
    def __init__(self):
        super(Disease, self).__init__()
    def get_disease(self):
        return diseases_dict


