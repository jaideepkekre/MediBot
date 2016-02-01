#!usr/bin/python
# Owner : Sameer Deshmukh
# _author_ = Sameer Deshmukh
# _info_   = Questions for rash.

def data():
    return 
    {
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
        }    
    }

def test():
    data()

if __name__ == '__main__':
    test()