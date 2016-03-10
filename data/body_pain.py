#!usr/bin/python
# Owner : Sameer Deshmukh
# _author_ = Sameer Deshmukh
# _info_   = Questions for body pain.

def data():
    return {
        'body_pain_head': {
            'question': "Does your Head hurt?",
            'response': ['Yes', 'No'],
            'response_type' : 'ruledchar',
            'serial' : 0,

        },

        'body_pain_chest': {
            'question': "Does your chest hurt?",
            'response': ['Yes', 'No'],
            'response_type': 'ruledchar',
            'serial': 1,

        },

        'body_pain_stomach': {
            'question': "Does your stomach area hurt?",
            'response': ['Yes', 'No'],
            'response_type': 'ruledchar',
            'serial': 2,

        },

        'body_pain_muscles': {
            'question': "Do your muscles hurt?",
            'response': ['Yes', 'No'],
            'response_type': 'ruledchar',
            'serial': 3,

        }

    }


if __name__ == '__main__':
    data()