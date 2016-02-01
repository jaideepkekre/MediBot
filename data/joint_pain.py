#!usr/bin/python
# Owner : Sameer Deshmukh
# _author_ = Sameer Deshmukh
# _info_   = Questions for join pain.

def data():
    return
    {
        'joint_pain_area' : {
            'question' : "Which joints hurt the most?",
            'response' : ['Knees', 'Elbows', 'Shoulders', 'Fingers'],
            'response_type' : 'ruledchar',
            'loop' : True,
            'serial' : 0,
            'linked_questions' : {
                'question' : "Are any other joins hurting?",
                'response' : ['Yes', 'No'],
                'response_type' : 'ruledchar',
                'tag' : 'joint_pain_area_more_pain'
            }
        }    
    }

if __name__ == '__main__':
    data()