#!usr/bin/python
# Owner :Jaideep Kekre
# _author_ = Jaideep Kekre
# _info_   =  Disease interface

"""
This module populates the buckets from symptom_validity_table.
This module contains the disease data .

"""
from symptom_validity_table import symptom_validity_table
CRITICAL = 20
IMPORTANT= 10
OPTIONAL = 5

"""
Critical symptom : 20 #Disease can't be characterized without this .
Important symptom: 10 #Important symptoms , common to multiple diseases.
Optional symptoms: 5  #Symptoms which the patient may not exhibit .


"""

class Buckets:
    def __init__(self):
        self.bucket  = dict()
        self.symptom_score= [0]*11
        self.symptom_index = dict()

        self.init_index()
        self.init_bucket()

        self.populate_dengue()
        self.populate_hepA()



    def init_index(self):
        self.symptom_index['fever']=0
        self.symptom_index['body_pain']=1
        self.symptom_index['joint_pain']=2
        self.symptom_index['pain_behind_eyes']=4
        self.symptom_index['rash']=5
        self.symptom_index['fatigue']=6
        self.symptom_index['loss_of_appetite']=7
        self.symptom_index['yellow_eyes']=8
        self.symptom_index['clay_coloured_bowels']=9
        self.symptom_index['nausea']=10
        #Add new symptom here
    def init_bucket(self):
        self.bucket['dengue']=None
        self.bucket['hepA']=None
        #Add new symptom here 

    def add_score(self,symptom,score,disease):
        self.symptom_score[self.symptom_index[symptom]] =  self.symptom_score[self.symptom_index[symptom]]+score
        disease.set_score(symptom,score)



    def populate_dengue(self):

        dengue = symptom_validity_table()
        dengue.set('fever', True)
        dengue.set('fever_measure', [105, 110])
        dengue.set('rash', True)
        dengue.set('body_pain', True)
        dengue.set('joint_pain', True)
        dengue.set('pain_behind_eyes', True)
        #
        self.add_score('fever',(IMPORTANT+CRITICAL),dengue)
        self.add_score('body_pain',IMPORTANT,dengue)
        self.add_score('joint_pain',IMPORTANT,dengue)
        self.add_score('pain_behind_eyes' ,OPTIONAL,dengue)
        self.add_score('rash',OPTIONAL,dengue)
        #
        self.bucket['dengue']=dengue
        """
        #dengue.set_score('fever', IMPORTANT)
        #dengue.set_score('fever_measure', CRITICAL)
        #dengue.set_score('body_pain', IMPORTANT)
        #dengue.set_score('joint_pain', IMPORTANT)
        #dengue.set_score('pain_behind_eyes', OPTIONAL)
        #dengue.set_score('rash',OPTIONAL)
        #
        """




    def populate_hepA(self):
        hepA = symptom_validity_table()
        hepA.set('fever', True)        
        hepA.set('fatigue', True)
        hepA.set('joint_pain', True)
        hepA.set('clay_coloured_bowels', True)
        hepA.set('yellow_eyes', True)
        #
        self.add_score('fever',(IMPORTANT),hepA)
        self.add_score('fatigue',IMPORTANT,hepA)
        self.add_score('joint_pain',IMPORTANT,hepA)
        self.add_score('clay_coloured_bowels' ,OPTIONAL,hepA)
        self.add_score('yellow_eyes',IMPORTANT,hepA)
        #
        self.bucket['hepA']=hepA

        





if __name__ == '__main__':
    bucketlist = Buckets()
    print(bucketlist.bucket)
    print(bucketlist.symptom_score)
    
