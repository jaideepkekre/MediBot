#!usr/bin/python
# Owner : Sameer Deshmukh
# _author_ = Sameer Deshmukh
# _info_   = Questions for join pain.
from Emoji import no
from Emoji import yes


def data():
    return {
        'joint_pain_knee': {
            'question': "Does your Knee hurt?",
            'response': [yes, no],
            'response_type' : 'ruledchar',
            'serial' : 0,

        },
        'joint_pain_hip': {
            'question': "Does your hip joint hurt?",
            'response': [yes, no],
            'response_type': 'ruledchar',
            'serial': 1,
        },
        'joint_pain_hand': {
            'question': "Does your hand joints hurt?",
            'response': [yes, no],
            'response_type': 'ruledchar',
            'serial': 2,
        },
        'joint_pain_shoulder': {
            'question': "Does your shoulder joint hurt?",
            'response': [yes, no],
            'response_type': 'ruledchar',
            'serial': 3,

            }
    }





if __name__ == '__main__':
    data()