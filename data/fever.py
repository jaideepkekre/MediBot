#!usr/bin/python
# Owner : Sameer Deshmukh
# _author_ = Sameer Deshmukh
# _info_   = Questions for fever.

def data():
    return {
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