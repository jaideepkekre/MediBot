#!usr/bin/python
# Owner : Sameer Deshmukh
# _author_ = Sameer Deshmukh
# _info_   = Top questions.
from Emoji import no
from Emoji import yes


def data():
    return  {
        'fever' : {
            'question' : "Do you have a fever?",
            'response' : ['Yes, High (> 103 F)', 'Yes, Mild (101-103 F)',
                          'Yes, Very Mild (99 - 101 F)', no],
            'response_type' : 'ruledchar',
        },
        'body_pain' : {
            'question' : "Do you have body pain?",
            'response': [yes, no],
            'response_type' : 'ruledchar',
        },
        'head_ache' : {
            'question' : "Do you have a head ache?",
            'response' : [yes, no],
            'response_type' : 'ruledchar'
        },
        'body_chills' : {
            'question' : "Are you experiencing body chills?",
            'response' : [yes, no],
            'response_type' : 'ruledchar'
        },
        'diarrhea' : {
            'question' : "Are you having very frequent loose motions?",
            'response' : [yes, no],
            'response_type' : 'ruledchar'
        },
        'consumed_contaminated_stuff' : {
            'question' : "Did you recently consume contaminated food or water?",
            'response' : [yes, no],
            'response_type' : 'ruledchar'
        },
        'extreme_weakness' : {
            'question' : "Are you experiencing extreme weakness?",
            'response' : [yes, no],
            'response_type' : 'ruledchar'
        },
        'rash' : {
            'question' : "Are you having a rash anywhere on your body?",
            'response': [yes, no],
            'response_type' : 'ruledchar',
        },
        'pain_behind_eyes' : {
            'question' : "Are you experiencing pain behind the eyes?",
            'response': [yes, no],
            'response_type' : 'ruledchar',
        },
        'joint_pain' : {
            'question' : "Are you having joint pain?",
            'response': [yes, no],
            'response_type' : 'ruledchar',
        },
        'fatigue' : {
            'question' : "Are you experiencing any fatigue?",
            'response': [yes, no],
            'response_type' : 'ruledchar'
        },
        'loss_of_appetite' : {
            'question' : "Are you having a loss of appetite?",
            'response': [yes, no],
            'response_type' : 'ruledchar'
        },
        'yellow_eyes' : {
            'question' : "Are you having yellowing of eyes?",
            'response': [yes, no],
            'response_type' : 'ruledchar'
        },
        'yellow_nails' : {
            'question' : "Are you having yellow nails?",
            'response' : [yes, no],
            'response_type' : 'ruledchar'
        },
        'clay_coloured_bowels' : {
            'question' : "Are you experiencing clay-coloured bowel movements?",
            'response': [yes, no],
            'response_type' : 'ruledchar'
        },
        'nausea' : {
            'question' : 'Are you experiencing nausea?',
            'response': [yes, no],
            'response_type' : 'ruledchar',
        },
    }

if __name__ == '__main__':
    d = data()
    print d['nausea']