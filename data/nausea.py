#!usr/bin/python
# Owner : Sameer Deshmukh
# _author_ = Sameer Deshmukh
# _info_   = Nausea top questions.

def data():
    return  {
        'nausea_vomiting' : {
            'question' : "Have you had any vomiting recently?",
            'response' : ['Yes','No'],
            'response_type' : 'ruledchar',
            'serial' : 0,
            'linked_questions' : {
                'question' : "Approximately how many vomiting episodes have you had in past 24 hours?",
                'response_type' : 'int',
                'custom_keyboard' : 'numpad',
                'tag' : 'nausea_vomiting_count'
            },
        },
    }

if __name__ == '__main__':
    data()