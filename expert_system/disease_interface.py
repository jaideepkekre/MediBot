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
        dengue.set('fever', True)
        dengue.set('fever_measure', [105, 110])

        dengue.set('rash', True)
        dengue.set('body_pain', True)
        dengue.set('joint_pain', True)
        dengue.set('pain_behind_eyes', True)

        dengue.set_score('fever', 10)
        dengue.set_score('fever_measure', 20)
        dengue.set_score('body_pain', 10)
        dengue.set_score('joint_pain', 10)
        dengue.set_score('pain_behind_eyes', 5)

        """
        Critical symptom : 20 #Disease can't be characterized without this .
        Important symptom: 10 #Important symptoms , common to multiple diseases.
        Optional symptoms: 5  #Symptoms which the patient may not exhibit .


        """




if __name__ == '__main__':
    bucketlist = InitBucket()
    bucketlist.populate_dengue()
