#!usr/bin/python
# Owner :Jaideep Kekre
# _author_ = Jaideep Kekre
# _info_   =  Disease interface

"""
This module populates the buckets from symptom_validity_table.
This module contains the disease data .

"""
from symptom_validity_table import symptom_validity_table
from disease import Disease 
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
        self.symptom_score = dict()
        self.populate_diseases()

        
    def add_symptom_score(self,symptom,score):
        if symptom in self.symptom_score.keys():
            self.symptom_score[symptom]=self.symptom_score[symptom]+score
        else :
            self.symptom_score[symptom]=score 
        
        #Add new symptom here
    

    def set_table(self,symptom,score,table_disease_object,arg=True):
        self.add_symptom_score(symptom, score)
        table_disease_object.set_score(symptom,score)
        table_disease_object.set(symptom,arg)
    
    def populate_diseases(self):
        diseases_object = Disease()
        diseases_dict=diseases_object.get_disease()
        for specific_disease_name in diseases_dict.keys():
            new_table_obj         = symptom_validity_table()
            specific_disease_dict = diseases_dict[specific_disease_name]
            for symptom in specific_disease_dict.keys():
                #print symptom
                if symptom == 'name':
                    print specific_disease_dict[symptom] + " : LOADED"

                else:
                    self.set_table(symptom,specific_disease_dict[symptom],new_table_obj)
            self.bucket[specific_disease_name]=new_table_obj
            


        





if __name__ == '__main__':
    bucketlist = Buckets()
    print "Contents of Bucket are :" + str((bucketlist.bucket))
    print(bucketlist.symptom_score)
    
