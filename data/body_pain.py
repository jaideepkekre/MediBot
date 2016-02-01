#!usr/bin/python
# Owner : Sameer Deshmukh
# _author_ = Sameer Deshmukh
# _info_   = Questions for body pain.

def data():
    return
    {
        'body_pain_area' : {
            'question' : "Where are you experiencing pain the most?",
            'response' : ['Head', 'Chest', 'Stomach', 'Hands', 'Legs'],
            'response_type' : 'ruledchar',
            'loop' : True,
            'serial' : 0,
            'linked_questions' : {
                'question' : "Are you still having body pain elsewhere?",
                'response' : ['Yes', 'No'],
                'response_type' : 'ruledchar',
                'tag' : 'body_pain_area_more_pain'
            }
        }
    }


if __name__ == '__main__':
    data()