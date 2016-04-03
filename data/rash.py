#!usr/bin/python
# Owner : Sameer Deshmukh
# _author_ = Sameer Deshmukh
# _info_   = Questions for rash.
from Emoji import yes, no

def data():
    return {
        'rash_area' : {
            'question' : "Where are you having a rash?",
            'response' : ['Face', 'Abdomen', 'Hands', 'Legs'],
            'response_type' : 'ruledchar',
            'loop' : True,
            'serial' : 0,
            'linked_questions' : {
                'question' : "Are you having rashes elsewhere?",
                'response' : ['Yes', 'No'],
                'response_type' : 'ruledchar',
                'tag' : 'rash_area_more_rash'
            }
        },
        'rose_spots' : {
            'question' : "Does your rash look like rose-coloured spots?",
            'response' : [yes, no],
            'response_type' : 'ruledchar',
            'serial' : 1
        }    
    }

def test():
    data()

if __name__ == '__main__':
    test()