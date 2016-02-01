#!usr/bin/python
# Owner : Sameer Deshmukh
# _author_ = Sameer Deshmukh
# _info_   = Questions for fever.

def data():
    return 
    {
        'fever_measure' : {
            'question' : "Please measure your fever with a thermometer and tell us your temperature.",
            'response_type' : ['int', 'float'],
            'ranged' : True,
            'range' : [95, 110],
            'custom_keyboard' : 'numpad',
            'serial' : 0,
        },
        'fever_periodic' : {
            'question' : "Are you having intermittent fever over time?",
            'response' : ['Yes', 'No'],
            'response_type' : 'ruledchar',
            'serial' : 1,
        }
    }

def test():
    data()

if __name__ == '__main__':
    test()