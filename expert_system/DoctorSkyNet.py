#!/usr/bin/python
"""
Owner = Jaideep Kekre
This module askes the questions
"""
from disease_interface import Buckets
from medibot_helper import bcolors, keywithmaxval
from question_interface import question_interface
from scratch_pad import scratch_pad
from tabled_mailer import mail_this



class DoctorSkyNet(object):
    def __init__(self, chat_id, db_connection):
        self.change_point_one = 0.3
        self.change_point_two = 0.6

        self.invalid_questions = list()

        self.last_asked_question = None
        self.response = None

        self.ask_this = None

        self.scratch_pad_object = scratch_pad()
        self.question_structure_dict = getattr(self.scratch_pad_object, 'data')
        self.basic_data_questions_table = self._create_basic_data_table()
        self.last_asked_basic_question = None
        self.email_table = list()

        self.bucket_object = Buckets()
        self.questions_asked = self.bucket_object.removed_questions_list
        self.fraction = 0
        self.db_connection = db_connection
        self.chat_id = chat_id

        self.stage_0 = self._verify_basic_questions_asked_and_set_answered()
        self.stage_1 = 0
        self.stage_2 = 0
        self.stage_3 = 0

        self.is_minus_one_done = 0
        self.is_zero_done = 0
        self.done = 0

    """
    sends mail using medibot_helper
    """

    def sendMail(self):
        lists = self.bucket_object.get_bucket_fraction_list()
        mail_this(self.email_table, self.chat_id, lists)

        pass

    """
    If all basic questions have been answered for this chat id, then this will
    set stage_0 to 1, meaning that basic questions have been answered.
    """
    def _verify_basic_questions_asked_and_set_answered(self):
        return_value = 1
        for attr in self.basic_data_questions_table:
            value = self.db_connection.get_basic_data_for_chat_id(self.chat_id, attr)
            if not value:
                return_value = 0
            else:
                self.basic_data_questions_table[attr] = value

        return return_value

    """
    create a dict (table) to see the basic data collection
    """
    def _create_basic_data_table(self):
        data_dict = {}

        for tag in __import__('basic_data').data().keys():
            data_dict[tag] = False

        return data_dict

    '''
    checks if the top question for the current question is asked , if asked then
    the question can be asked else the top question is asked instead
    '''
    def update_fractions(self):
        self.fraction = self.bucket_object.get_avg_fraction()

    def check_if_top_asked(self, question):
        # first check if the question is a top question
        if question is None:
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
        self.email_table.append([self.last_asked_question, self.response])

        self.bucket_object.answered_question_True(self.last_asked_question,
                                                  self.response, self.db_connection, self.chat_id)
        if self.response == 'No' or self.response == 'False':
            self.invalidate_question(self.last_asked_question)

    def next_question(self):
        self.update_fractions()
        print bcolors.FAIL + str(self.fraction)
        print bcolors.OKBLUE
        if self.bucket_object.done == 1:
            self.done == 1
            return None
        """
        algo -1 , 0 here
        """
        if self.is_minus_one_done == 0:
            self.is_minus_one_done = 1
            symptom = self.algorithm_minus_one()
            if symptom is not None:
                return self.create_question(symptom)
        if self.is_zero_done == 0:
            self.is_zero_done = 1
            symptom = self.algorithm_zero()
            if symptom is not None:
                return self.create_question(symptom)

        '''
        algorithm 1,2,3 start from here
        '''
        if (self.fraction < self.change_point_one):
            self.ask_this = self.algorithm_one()
            if self.ask_this is None:
                self.ask_this = self.algorithm_two()

                if self.ask_this is None:
                    self.ask_this = self.algorithm_three()
                    if self.ask_this is None:
                        self.done = 1

        elif self.fraction < self.change_point_two:
            self.ask_this = self.algorithm_two()
            if self.ask_this is None:
                self.ask_this = self.algorithm_three()
        else:
            self.ask_this = self.algorithm_three()
            if self.ask_this is None:
                self.done = 1
                # SEND MAIL HERE
                # print "None caught in 33"

        if self.done == 0:
            q = self.check_if_top_asked(self.ask_this)
            if q is None:
                # print "None captured in 3"
                return self.create_question(self.ask_this)
            else:
                return self.create_question(q)
        else:
            print "Done"
            return None

    """
    ask the question which will fill the most buckets.
    """
    def algorithm_one(self):
        question = self.bucket_object.get_popular_symptoms()
        print bcolors.WARNING + "using algo-1-"
        print bcolors.OKBLUE
        if question is None:
            print "None in algo one:"
            return None
        return question

    """
    ask critical questions so that buckets can be eliminated fast.
    """
    def algorithm_two(self):
        question = self.bucket_object.get_top_critical_symptoms()
        print bcolors.WARNING + "Using algo-2-"
        print bcolors.OKBLUE
        if question is None:
            print "None in algo two"
            return None
        return question

    """
    ask the question which will fill up the remaining buckets the fastest.
    """
    def algorithm_three(self):
        question = self.bucket_object.get_buckets_top_symptom()
        print bcolors.WARNING + "using algo-3-"
        print bcolors.OKBLUE
        if question is None:
            print "None in algo three"
            self.done = 1
            return None
        return question

    """
    returns the most common historical symptom for all patients
    """

    def algorithm_minus_one(self):
        symptom_dict = self.db_connection.get_global_symptom_count()
        done_list = self.bucket_object.get_asked_questions()
        print "Global:"
        print bcolors.FAIL + str(symptom_dict)
        print bcolors.OKBLUE
        for symptom in done_list:
            symptom_dict.pop(symptom)

        not_zero_flag = 0

        for data in symptom_dict.values():
            if data != '0':
                not_zero_flag = 1
                break
        if not_zero_flag == 0:
            print bcolors.FAIL + "No historical data found!"
            print bcolors.OKBLUE
            return None

        else:
            top_symptom = keywithmaxval(symptom_dict)
            print bcolors.FAIL + "Global Historical Data found, using:" + top_symptom
            print bcolors.OKBLUE
            return top_symptom

    """
    returns the most common historical symptom for THIS patient
    """

    def algorithm_zero(self):
        symptom_dict = self.db_connection.get_symptom_data_for_chat_id(self.chat_id)
        done_list = self.bucket_object.get_asked_questions()
        for symptom in done_list:
            symptom_dict.pop(symptom)

        print bcolors.FAIL + str(symptom_dict)
        print bcolors.OKBLUE
        not_zero_flag = 0
        for data in symptom_dict.values():
            if data != '0':
                not_zero_flag = 1
                break
        if not_zero_flag == 0:
            print bcolors.FAIL + "No historical data found for this user!"
            print bcolors.OKBLUE
            return None

        else:
            top_symptom = keywithmaxval(symptom_dict)
            print bcolors.FAIL + "Personal Historical Data found, using:" + top_symptom
            print bcolors.OKBLUE
            return top_symptom



    def create_question(self, question):
        q_obj = question_interface()
        q_obj = q_obj.return_question(question)
        # print bcolors.HEADER+q_obj.question
        # print q_obj.response
        #print bcolors.OKBLUE
        # print question
        self.last_asked_question = question
        return q_obj


    """
    invalidates the linked question if top question is false
    """
    def invalidate_question(self, question):
        if question is None:
            return None
        if question in self.question_structure_dict.keys():
            lista = self.question_structure_dict[question]

            if len(lista) > 0:
                for questions in lista:
                    if questions is None:
                        pass
                    #print question + " invalidated" + " for response " + self.response
                    self.bucket_object.answered_question_True(question, False, None, None)

    def next_basic_data_question(self):
        next_question = None
        for tag in self.basic_data_questions_table:
             if not self.basic_data_questions_table[tag]:
                next_question = tag
                self.last_asked_basic_question = tag
                break

        if next_question is None:
            return None

        question_dict = __import__('basic_data').data()[next_question]
        q_obj = question_interface()
        q_obj.question = question_dict['question']
        q_obj.response = question_dict['response']
        q_obj.response_type = question_dict['response_type']

        return q_obj

    def askdoctor(self, response=None):
        if response is not None:
            self.response = response
        self.update_fractions()
        self.stage_1 = 1 # state just for future proofing. No use right now.
        """
        BASIC QUESTION LOGIC
        """
        if self.stage_0 != 1: # basic question asking logic
            if self.last_asked_basic_question:
                self.basic_data_questions_table[self.last_asked_basic_question] = self.response

            q_obj = self.next_basic_data_question()
            if q_obj is None:
                self.stage_0 = 1
                self.response = None

                # this should be the only place where all the basic data is set
                for attr, value in self.basic_data_questions_table.iteritems():
                    self.db_connection.set_basic_data_for_chat_id(self.chat_id, attr, value)
            else:
                return q_obj
        """
        NORMAL QUESTION LOGIC
        """

        if self.done == 1:
            print "DONE"
            return None
        elif self.stage_1 == 1 and self.stage_0 == 1 and self.done == 0:
            if self.last_asked_question is None and self.response is None:
                q_obj = self.next_question()
            else:
                self.send_last_question_details()
                q_obj = self.next_question()
            if q_obj is None:
                self.done = 1
                print "All Questions done!"
                self.sendMail()
                return None
            else:
                return q_obj



if __name__ == '__main__':
    obj = DoctorSkyNet()
    obj.askdoctor()

    obj.askdoctor("Yes, High (> 103 F)")

    obj.askdoctor("No")

    obj.askdoctor("Yes")
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
