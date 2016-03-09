#!/usr/bin/python
"""
Owner = Jaideep Kekre
This module askes the questions
"""
from disease_interface import Buckets
from question_interface import question_interface
from scratch_pad import scratch_pad


class DoctorSkyNet(object):
    def __init__(self):
        self.stage_0 = 0
        self.stage_1 = 0
        self.stage_2 = 0
        self.stage_3 = 0
        self.done = 0

        self.change_point_one = 0.3
        self.change_point_two = 0.6

        self.invalid_questions = list()

        self.last_asked_question = None
        self.response = None

        self.ask_this = None

        self.scratch_pad_object = scratch_pad()
        self.question_structure_dict = self.scratch_pad_object._build_data()

        self.bucket_object = Buckets()
        self.questions_asked = self.bucket_object.removed_questions_list
        self.fraction = 0

    '''
    checks if the top question for the current question is asked , if asked then the question can be asked else
    the top question is asked instead
    '''

    def update_fractions(self):
        self.fraction = self.bucket_object.get_avg_fraction()

    def check_if_top_asked(self, question):
        # first check if the question is a top question
        if question == None:
            print "none in invalid"
            return None
        if question in self.question_structure_dict.keys():
            # print "this is top question , no worry"
            return question
        else:
            for top_question in self.question_structure_dict.keys():
                list = self.question_structure_dict[top_question]
                if question in list:
                    if top_question in self.questions_asked:
                        return question
                    else:
                        return top_question

    def send_last_question_details(self):
        # print "sending:" + self.last_asked_question
        # print "sending"  + self.response
        self.bucket_object.answered_question_True(self.last_asked_question, self.response)
        if self.response == 'No' or self.response == 'False':
            self.invalidate_question(self.last_asked_question)

    def next_question(self):
        self.update_fractions()
        print self.fraction
        if self.bucket_object.done == 1:
            self.done == 1
            return None
        if (self.fraction < self.change_point_one):
            self.ask_this = self.algorithm_one()
            if self.ask_this == None:
                self.ask_this = self.algorithm_two()

        elif self.fraction < self.change_point_two:
            self.ask_this = self.algorithm_two()
            if self.ask_this == None:
                self.ask_this = self.algorithm_three()
        else:
            self.ask_this = self.algorithm_three()
            if self.ask_this == None:
                self.done = 1
                # print "None caught in 33"

        if self.done == 0:
            q = self.check_if_top_asked(self.ask_this)
            if q == None:
                # print "None captured in 3"
                return self.create_question(self.ask_this)
            else:
                return self.create_question(q)
        else:
            print "Done"
            return None

    def algorithm_one(self):
        question = self.bucket_object.get_popular_symptoms()
        print "using algo-1-"
        if question == None:
            print "None in algo one:"
            return None
        return question[0]

    def algorithm_two(self):
        question = self.bucket_object.get_top_critical_symptoms()
        print "Using algo-2-"
        if question == None:
            print "None in algo two"
            return None
        return question[0]

    def algorithm_three(self):
        question = self.bucket_object.get_buckets_top_symptom()
        print "using algo-3-"
        if question == None:
            print "None in algo three"
            return None
        return question[0]

    def create_question(self, question):
        q_obj = question_interface()
        q_obj = q_obj.return_question(question)
        print q_obj.question
        print q_obj.response
        # print question
        self.last_asked_question = question
        return q_obj

    def invalidate_question(self, question):
        if question == None:
            return None
        if question in self.question_structure_dict.keys():
            lista = self.question_structure_dict[question]

            if len(lista) > 0:
                for questions in lista:
                    if questions == None:
                        pass
                    #print question + " invalidated" + " for response " + self.response
                    self.bucket_object.answered_question_True(question, False)

    def askdoctor(self, response=None):
        if response != None:
            self.response = response
        self.update_fractions()
        self.stage_0 = 1
        self.stage_1 = 1
        if self.done == 1:
            print "DONE"
            return None
        elif self.stage_1 == 1 and self.stage_0 == 1 and self.done == 0:
            if self.last_asked_question == None and self.response == None:
                q_obj = self.next_question()
            else:
                self.send_last_question_details()
                q_obj = self.next_question()
            if q_obj == None:
                self.done =1
                print "All Questions done!"



if __name__ == '__main__':
    obj = DoctorSkyNet()
    obj.askdoctor()
    obj.askdoctor("No")

    obj.askdoctor("No")

    obj.askdoctor("No")
    obj.askdoctor("No")
    obj.askdoctor("No")
    obj.askdoctor("Yes")
    obj.askdoctor("Yes")
    obj.askdoctor("No")
    obj.askdoctor("Yes")
    obj.askdoctor("Yes")
    obj.askdoctor("Yes")
    obj.askdoctor("Yes")
    obj.askdoctor("Yes")
    obj.update_fractions()
    print obj.fraction
    # print obj.last_asked_question
    # print obj.response
    print "***"
