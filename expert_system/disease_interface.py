#!usr/bin/python
# Owner :Jaideep Kekre
# _author_ = Jaideep Kekre
# _info_   =  Disease interface

"""
This module populates the buckets from symptom_validity_table.
This module contains funtions to interact with diseases .

"""
import heapq

from disease import Disease
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
        self.symptom_score = dict()
        self.symptom_critical_count = dict()
        self.disease_score = dict()
        self.diseases_object = Disease()
        self.removed_questions_list = list()

        self.populate_diseases()


    """
    <------------------------PUBLIC METHODS TO BY CALLED BY OUTSIDE MODULES----------------->
    """
    def get_score_by_symptom(self,symptom):
        if symptom in self.removed_questions_list:
            return None
        elif symptom in self.symptom_score.keys():
            return self.symptom_score[symptom]
        else:
            return None

    def get_score_by_disease(self,disease_name):
        if disease_name in self.bucket.keys():
            self.calculate_current_score(disease_name)
            return self.disease_score[disease_name]
        else:
            return None
        pass

    """
    """

    def get_top_symptoms(self, number_of_symptoms):
        top_symptoms = heapq.nlargest(number_of_symptoms, self.symptom_score, key=self.symptom_score.get)
        return top_symptoms

    """
    get_top_critical_symptoms
    returns list of top n critical symptoms across diseases
    """

    def get_top_critical_symptoms(self, number_of_symptoms):
        top_symptoms = heapq.nlargest(number_of_symptoms, self.symptom_critical_count,
                                      key=self.symptom_critical_count.get)
        return top_symptoms

    def remove_disease(self, name):
        if name in self.bucket.keys():
            diseases_dict = self.diseases_object.get_disease()
            for specific_disease_name in diseases_dict.keys():
                if name == specific_disease_name:
                    disease_dict = diseases_dict[specific_disease_name]
                    for symptom in disease_dict.keys():
                        if symptom in self.removed_questions_list:
                            pass
                        else:
                            self.remove_symptom_score(symptom, disease_dict)
                    self.bucket.pop(disease_dict['name'])
                    self.disease_score.pop(disease_dict['name'])

        pass

    def question_asked(self, symptom):

        for table_disease_object in self.bucket.values():
            table_disease_object.set_score(symptom, 0)
            table_disease_object.set(symptom, False)
        if symptom in self.symptom_score.keys():
            self.symptom_score.pop(symptom)
        if symptom in self.symptom_critical_count.keys():
            self.symptom_critical_count.pop(symptom)
        for disease_name in self.bucket.keys():
            self.calculate_current_score(disease_name)
        self.removed_questions_list.append(symptom)






    """
    <---------------------------------------INTERNAL METHODS-------------------------------->
    """

    """
    calculate_current_score()
    calculates total score for the given disease
    """
    def calculate_current_score(self,disease_name):
        if disease_name in self.bucket.keys():
            list_disease_dict=self.diseases_object.get_disease()
            specific_disease_dict=list_disease_dict[disease_name]
            table_disease_object=self.bucket[disease_name]
            score=0
            for symptom in specific_disease_dict.keys():
                if symptom == 'name':
                    pass
                elif symptom in self.removed_questions_list:
                    pass
                else:
                    temp=table_disease_object.get_score(symptom)
                    score=score+temp
            self.disease_score[disease_name]=score

    """
    add_symptom_score()
    adds score across diseases by symptoms
    """
    def add_symptom_score(self,symptom,score):
        if symptom in self.symptom_score.keys():
            self.symptom_score[symptom]=self.symptom_score[symptom]+score
        else :
            self.symptom_score[symptom] = score

    def update_critical_count(self, symptom):
        if symptom in self.symptom_critical_count.keys():
            self.symptom_critical_count[symptom] = self.symptom_critical_count[symptom] + 1
        else:
            self.symptom_critical_count[symptom] = 1



    def remove_symptom_score(self,symptom,disease_dict):
        if disease_dict[symptom] == None : 
            print "symptom already asked , hence ignore"
        elif symptom == 'name':
            pass
        else:
            self.symptom_score[symptom]=self.symptom_score[symptom]-disease_dict[symptom]
            if disease_dict[symptom] == CRITICAL:
                self.symptom_critical_count[symptom] = self.symptom_critical_count[symptom] - 1

    def remove_symptom(self,symptom,disease_dict):

        self.remove_symptom_score(symptom, score)

    """
    set_table():
    works on per symptom basis
    adds symptom score to total symptom score ie
    sets symptom to True in symptom validity table
    set symptom score in symptom validity table

    calls : add_symptom_score()
          : update_critical_count()
          : set_score()
          : set()

    called by
          : populate_diseases
    """
    def set_table(self,symptom,score,table_disease_object,arg=True):
        table_disease_object.set_score(symptom,score)
        table_disease_object.set(symptom,arg)
        if table_disease_object.get_score(symptom) == CRITICAL:
            self.update_critical_count(symptom)
        self.add_symptom_score(symptom, score)

    """
    populate_diseases()
    poplulates diseases from db and sets in the symptom validity table
    also adds the sypmtom validity object to the bucket dict

    """
    def populate_diseases(self):
        
        diseases_dict=self.diseases_object.get_disease()
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
            self.calculate_current_score(specific_disease_dict['name'])

            


        





if __name__ == '__main__':
    bucketlist = Buckets()
    print "Contents of Bucket are :" + str((bucketlist.bucket))
    print(bucketlist.symptom_score)
    #bucketlist.get_score_by_disease('dengue')

    print(bucketlist.get_score_by_disease('hepA'))
    print(bucketlist.get_score_by_disease('dengue'))
    print "*******************************"
    bucketlist.question_asked('fever')
    print(bucketlist.get_score_by_disease('hepA'))
    print(bucketlist.get_score_by_disease('dengue'))

    bucketlist.get_score_by_symptom('fever')
    bucketlist.remove_disease('dengue')
    bucketlist.remove_disease('dengue')
    bucketlist.remove_disease('dengue')
    #bucketlist.get_score_by_disease('dengue')
    #bucketlist.get_score_by_disease('hepA')
    # print "Contents of Bucket are :" + str((bucketlist.bucket))
    # print(bucketlist.symptom_score)
    # print (bucketlist.disease_score)
    # lista = bucketlist.get_top_critical_symptoms(3)
    # listb = bucketlist.get_top_symptoms(3)
    # print lista
    # print listb
    # bucketlist.remove_disease('hepA')
    # listc = bucketlist.get_top_critical_symptoms(3)
    # listd = bucketlist.get_top_symptoms(3)
    # print listc
    # print listd
    # print bucketlist.symptom_critical_count
    # print bucketlist.symptom_score
