#!usr/bin/python
# Owner : Sameer Deshmukh
# _author_ = Sameer Deshmukh
# _info_   = Contains data for the expert system.

def question_data():
    return {
        'fever' : {
            'question' : "Do you have a fever?",
            'response' : ['Yes', 'No'],
            'response_type' : 'ruledchar',
            'linked_questions' : {
                'question' : "Please measure your fever with a thermometer and tell us your temperature.",
                'response_type' : ['int', 'float'],
                'ranged' : True,
                'range' : [95, 110],
                'custom_keyboard' : 'numpad',
                'linked_questions' : {
                    'question' : "Are you having intermittent fever over time?",
                    'response' : ['Yes', 'No'],
                    'response_type' : 'ruledchar',
                    'tag' : 'periodic_fever' # is a character of malaria
                }
            }
        },

        'body_pain' : {
            'question' : "Do you have body pain?",
            'response' : ['Yes', 'No'],
            'response_type' : 'ruledchar',
            'linked_questions' : {
                'question' : "Where are you experiencing pain the most?",
                'response' : ['Head', 'Chest', 'Stomach', 'Hands', 'Legs'],
                'response_type' : 'ruledchar',
                'loop' : True,
                'linked_questions' : {
                    'question' : "Are you still having body pain elsewhere?",
                    'response' : ['Yes', 'No'],
                    'response_type' : 'ruledchar'
                }
            }
        },

        'rash' : {
            'question' : "Are you having a rash anywhere on your body?",
            'response' : ['Yes', 'No'],
            'response_type' : 'ruledchar',
            'linked_questions' : {
                'question' : "Where are you having a rash?",
                'response' : ['Face', 'Abdomen', 'Hands', 'Legs'],
                'response_type' : 'ruledchar',
                'loop' : True,
                'linked_questions' : {
                    'question' : "Are you having rashes elsewhere?",
                    'response' : ['Yes', 'No'],
                    'response_type' : 'ruledchar'
                }
            }
        },

        'pain_behind_eyes' : {
            'question' : "Are you experiencing pain behind the eyes?",
            'response' : ['Yes', 'No'],
            'response_type' : 'ruledchar'
        },

        'joint_pain' : {
            'question' : "Are you having joint pain?",
            'response' : ['Yes', 'No'],
            'response_type' : 'ruledchar',
            'linked_questions' : {
                'question' : "Which joints hurt the most?",
                'response' : ['Knees', 'Elbows', 'Shoulders', 'Fingers'],
                'response_type' : 'ruledchar',
                'loop' : True,
                'linked_questions' : {
                    'question' : "Are any other joins hurting?",
                    'response' : ['Yes', 'No'],
                    'response_type' : 'ruledchar'
                }
            }
        },

        'fatigue' : {
            'question' : "Are you experiencing any fatigue?",
            'response' : ['Yes', 'No'],
            'response_type' : 'ruledchar'
        },

        'loss_of_appetite' : {
            'question' : "Are you having a loss of appetite?",
            'response' : ['Yes', 'No'],
            'response_type' : 'ruledchar'
        },

       'yellow_eyes' : {
           'question' : "Are you having yellowing of eyes?",
           'response' : ['Yes', 'No'],
           'response_type' : 'ruledchar'
       },
 
       'clay_coloured_bowels' : {
           'question' : "Are you experiencing clay-coloured bowel movements?",
           'response' : ['Yes', 'No'],
           'response_type' : 'ruledchar'
       },
 
       'nausea' : {
           'question' : 'Are you experiencing nausea?',
           'response' : ['Yes', 'No'],
           'response_type' : 'ruledchar',
           'linked_questions' : {
               'question' : "Have you had any vomiting recently?",
               'response' : ['Yes','No'],
               'response_type' : 'ruledchar',
               'linked_questions' : {
                   'question' : "Approximately how many vomiting episodes have you had in past 24 hours?",
                   'response_type' : 'int',
                   'custom_keyboard' : 'numpad',
               },
           },
       },
   }


def test():
    d = question_data()
    print d['fever']['question']

if __name__ == '__main__':
    test()
