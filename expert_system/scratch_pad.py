#!usr/bin/python
# Owner : @v0dro
# _author_ =  @v0dro
# _info_   = Scratch pad for keeping track of which questions have been asked
#   and their status.
from symptom_validity_table import symptom_validity_table

class scratch_pad():
    """
    This class helps in keeping track of symptoms that have been detected in
    the user. The scratch pad will be built dynamically from the questions
    database kept in the data/ folder.

    'None' says that the question has not been answered at all. True says that
    the symptom is present, False says that it is absent altogether.

    The data is primarily reffered to and infered from 2 data structures:
    * symptom_validity_table
        This is a table, or rather a separate class that contains key value
        pairs denoting symtpom tag vs. its truth value. The value can be
        either None, True or False. See the symptom_validity_table() class 
        for more details on this.
    * data
        This is an internal DS that stores the top level tags as the key, the
        corresponding value is a list that contains the sub symptoms of the key.

        In case of nested questions the tags are kept inside a list, the elements
        of the list being the question tags in the order that they should be asked.
        The data is structured as follows:
        {
            'fever' : ['fever_periodic', 'fever_measure'],
            'body_pain' : [['body_pain_area', 'body_pain_area_more_pain']]
        }
    """
    def __init__(self):
        self.data = None
        self.symptom_validity_table = symptom_validity_table()
        self._build_data()

    def _build_data(self):
        self.data = dict()
        top_tags = __import__('top_questions').data().keys()

        for top_tag in top_tags:
            self.data[top_tag] = list()
            sub_tags_data_dict = __import__(top_tag).data()

            for sub_tag, sub_tag_data in sub_tags_data_dict.iteritems():
                self.data[sub_tag] = None

                while sub_tag_data.has_key('linked_questions'):
                    sub_tag_data = sub_tag_data['linked_questions']
                    linked_tag = sub_tag_data['tag']
                    self.data[linked_tag] = None

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

    table = getattr(sp, 'symptom_validity_table')

    if str(table.__class__) == 'symptom_validity_table.symptom_validity_table':
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
