#!usr/bin/python
# Owner : @v0dro
# _author_ =  @v0dro
# _info_   = Scratch pad for keeping track of which questions have been asked
#   and their status.

class scratch_pad():
    """
    This class helps in keeping track of symptoms that have been detected in
    the user. The scratch pad will be built dynamically from the questions
    database kept in the data/ folder.

    'None' says that the question has not been answered at all. True says that
    the symptom is present, False says that it is absent altogether.

    It does by storing them in a nested dict. Example,
    {
        'fever' : {
            'status' : None, # None if not yet asked, True if yes, False if not
            'fever_measure' : {
                'status' : None
            },
            'fever_periodic' : {
                'status' : None
            }
        },
        'joint_pain' : {
            'status' : None,
            'joint_pain_area' : {
                'status' : None,
                'joint_pain_area_more_pain' : {
                    'status' : None
                }
            }
        }
    }
    """
    def __init__(self):
        self.data = None
        self._build_scratch_pad()


    def _build_scratch_pad(self):
        self.data = dict()
        for tag in __import__('top_questions').data().keys():
            self.data[tag] = dict()

        for top_tag in self.data:
            tag_scratch_pad = self.data[top_tag]
            tag_scratch_pad['status'] = None
            sub_tags_data_dict = __import__(top_tag).data()

            for sub_tag, sub_tag_data in sub_tags_data_dict.iteritems():
                tag_scratch_pad[sub_tag] = {}
                tag_scratch_pad[sub_tag]['status'] = None
                temp = sub_tag_data
                sub_tag_scratch = tag_scratch_pad[sub_tag]

                while sub_tag_data.has_key('linked_questions'):
                    sub_tag_data = sub_tag_data['linked_questions']

                    linked_tag = sub_tag_data['tag']
                    sub_tag_scratch[linked_tag] = {}
                    sub_tag_scratch[linked_tag]['status'] = None

                    sub_tag_scratch = sub_tag_scratch[linked_tag]

    """
    Send a list of tags and sub tags to check status.

    The tags listed in the list should be nested. If at the end of the traversal
    more nested dicts are detected, a list containing the names of sub-tags which
    have 'status' set to 'None' will be returned.

    If the second optional argument is passed as True, then only the status of 
    the top level tag will be checked and returned. Function will not dive 
    further.

    Example:
        query(['fever'])
        # => ['fever_periodic', 'fever_measure']

        query(['fever'], True)
        # => None

        query(['fever', 'fever_periodic'])
        # => None
    """
    def query(self, tag_list, only_top_tag=False):
        if len(tag_list) > 2:
            raise AttributeError("Cannot have hierarchy deeper than 2.")

        if only_top_tag:
            return self.data[tag_list[0]]['status']

        temp = self.data[tag_list[0]]

        if len(tag_list) == 2:
            return temp[tag_list[1]]['status']
        
        return_tag_list = list()
        for inner_tag in temp:
            if inner_tag != 'status' and temp[inner_tag]['status'] == None:
                return_tag_list.append(inner_tag)                

        if len(return_tag_list) == 0:
            return None

        return return_tag_list

    """
    Use this method for setting the status of a given tag/sub-tag combination.
    If an incomplete tag list is specified, the status field of the last tag
    in the list will be set to True (default).

    Example:
        set(['fever'])
        # This will set ['fever']['status'] to True

        set(['fever', 'fever_periodic'])
        # This will set ['fever']['status'] and ['fever']['fever_periodic']['status']
        # to True
    """
    def set(self, tag_list, status=True):
        temp = self.data
        for tag in tag_list:
            temp = temp[tag]
            temp['status'] = status

if __name__ == '__main__':
    sp = scratch_pad()

    d = getattr(sp, 'data')
    if d['fever']['status'] == None and d['joint_pain']['joint_pain_area']['joint_pain_area_more_pain']['status'] == None:
        print "PASS1"

    if sp.query(['fever']) == ['fever_periodic', 'fever_measure']:
        print "PASS2"

    if sp.query(['fever'], True) == None:
        print "PASS3"

    sp.set(['fever'])
    if sp.query(['fever'], True) == True:
        print "PASS4"

    sp.set(['fever', 'fever_measure'])
    print sp.query(['fever', 'fever_measure'])
    print sp.query(['fever'])
    if sp.query(['fever', 'fever_measure']) == True and sp.query(['fever', 'fever_periodic']) == None \
    and sp.query(['fever']) == ['fever_periodic']:
        print "PASS5"


    sp.set(['joint_pain', 'joint_pain_area'])
    d = getattr(sp, 'data')

    if d['joint_pain']['status'] == True and d['joint_pain']['joint_pain_area']['status'] == True:
        print "PASS6"
