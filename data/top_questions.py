#!usr/bin/python
# Owner : Sameer Deshmukh
# _author_ = Sameer Deshmukh
# _info_   = Top questions.

def data():
    return  {
        'fever' : {
            'question' : "Do you have a fever?",
            'response' : ['Yes', 'No'],
            'response_type' : 'ruledchar',
        },
        'body_pain' : {
            'question' : "Do you have body pain?",
            'response' : ['Yes', 'No'],
            'response_type' : 'ruledchar',
        },
        'rash' : {
            'question' : "Are you having a rash anywhere on your body?",
            'response' : ['Yes', 'No'],
            'response_type' : 'ruledchar',
        },
        'pain_behind_eyes' : {
            'question' : "Are you experiencing pain behind the eyes?",
            'response' : ['Yes', 'No'],
            'response_type' : 'ruledchar',
        },
        'joint_pain' : {
            'question' : "Are you having joint pain?",
            'response' : ['Yes', 'No'],
            'response_type' : 'ruledchar',
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
        },
    }

if __name__ == '__main__':
    d = data()
    print d['nausea']