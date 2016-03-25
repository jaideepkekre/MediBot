#!usr/bin/python
# Owner : Sameer Deshmukh
# _author_ = Sameer Deshmukh
# _info_   = Questions for basic data.

def data():
    return {
        'age' : {
            'question' : "What is your age?",
            'response' : ['0-15', '15-25', '25-40', '40-50', '>50'],
            'response_type' : 'ruledchar',
            'serial' : 0
        },
        'height' : {
            'question' : "What is your height?",
            'response' : ['4-5 ft', '5-6 ft', '6-7 ft'],
            'response_type' : 'ruledchar',
            'serial' : 1
        },
        'weight' : {
            'question' : "What is your weight?",
            'response' : ['30-40 kg', '40-50 kg', '50-70 kg', '70-90 kg', '>90 kg'],
            'response_type' : 'ruledchar',
            'serial' : 2
        },
        'gender' : {
            'question' : "What is your gender?",
            'response' : ['Male', 'Female', 'Unspecified'],
            'response_type' : 'ruledchar',
            'serial' : 3
        }
    }

if __name__ == '__main__':
    data()