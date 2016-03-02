#!usr/bin/python
# Owner :Jaideep Kekre
# _author_ = Jaideep Kekre
# _info_   =  Disease interface

"""
This module populates the buckets from symptom_validity_table

"""
from symptom_validity_table import symptom_validity_table


class InitBucket:
    def __init__(self):
        self.disease_list = list()

    def populate_dengue(self):
        dengue = symptom_validity_table()
        dengue.set('fever', '>101')
        dengue.set('rash', True)
        dengue.set('body_pain', True)
        dengue.set('joint_pain', True)
        dengue.set('pain_behind_eyes', True)
        dengue.set('pain_behind_eyes', True)


if __name__ == '__main__':
    bucketlist = InitBucket()
    bucketlist.populate_dengue()
