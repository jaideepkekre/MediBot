#!/usr/bin/python
"""
Owner : Jaideep Kekre

This module stores the  Other symptom state on a per disease level, rest are 
automatically set to True

Works for : FEVER
"""
from disease import Disease


class Disease_Signature(object):
    def __init__(self):
        disease_object_home = Disease()
        disease_dict_home = disease_object_home.get_disease()

        self.hepA = 'hepA'
        self.dengue = 'dengue'
        self.malaria = 'malaria'
        self.typhoid_fever = 'typhoid_fever'
        self.leptospirosis = 'leptospirosis'
        self.fever_states = ['Yes, High (> 103 F)', 'Yes, Mild (101-103 F)', 'Yes, Very Mild (99 - 101 F)', 'No']
        # print self.fever_states[0]

        self.fever = {
            self.dengue: self.fever_states[0],
            self.hepA: self.fever_states[1],
            self.malaria : self.fever_states[0],
            self.typhoid_fever : self.fever_states[0],
            self.leptospirosis : self.fever_states[1]
        }

    def get_fever(self, disease_name):
        return self.fever[disease_name]


if __name__ == "__main__":
    obj = Disease_Signature()
    print obj.get_fever('hepA')
