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
        self.top_tags = __import__('top_questions').data().keys()
        self._build_data()

    def _build_data(self):
        self.data = dict()
        
        for top_tag in self.top_tags:
            self.data[top_tag] = list()
            sub_tags_data_dict = __import__(top_tag).data()
            size = len(sub_tags_data_dict)

            # aligns questions by serial because python does not guarantee order
            #   of dict :\
            for serial in range(0,size):
                inner_tag = None
                eventual_data = None
                for t in sub_tags_data_dict:
                    if sub_tags_data_dict[t]['serial'] == serial:
                        inner_tag = t
                        break

                eventual_data = inner_tag

                self.data[top_tag].append(eventual_data)
        return self.data

    """
    Send a list of tags and sub tags to check status.

    If the second optional argument is passed as True, then only the status of 
    the top level tag will be checked and returned. Function will not dive 
    further.

    Example:
        query('fever')
        # => 'fever_periodic'

        set('fever_measure')
        query('fever')
        # => 'fever_measure'

        query('fever_periodic')
        # => None
    """
    def query(self, tag, only_top_tag=False):
        if tag in self.top_tags:
            if only_top_tag:
                return self.symptom_validity_table.get(tag)

            return self.data[tag]

        return self.symptom_validity_table.get(tag)

    """
    Use this method for setting the status of a given tag/sub-tag combination.
    If an incomplete tag list is specified, the status field of the last tag
    in the list will be set to True (default).

    Example:
        set('fever')
        # This will set 'fever' to True
    """
    def set_top_level(self, tag, status=True):
        if tag in self.top_tags:
            self.symptom_validity_table.set(tag, status)
        else:
            raise AttributeError("bad..bad input " + tag)

    """
    This will remove the first sub_tag from the tags dict
    """
    def pop(self, tag):
        popped = self.data[tag].pop(0)
        if type(popped) == list:
            for pop in popped:
                self.symptom_validity_table.set(pop)
        else:
            self.symptom_validity_table.set(popped)

    """
    Remove a specific sub tag from top tag dict.
    """
    def pop_specific(self, tag_hierarchy):
        tag_list = self.data[tag_hierarchy[0]]
        index = None

        for idx, tag in enumerate(tag_list):
            if type(tag) == list:
                if tag_hierarchy[1] == tag[0]:
                    index = idx
                    break
            else:
                if tag_hierarchy[1] == tag:
                    index = idx
                    break

        popped = tag_list[index]
        if type(popped) == list:
            for pop in popped:
                self.symptom_validity_table.set(pop)
        else:
            self.symptom_validity_table.set(popped)

        del tag_list[index]


if __name__ == '__main__':
    sp = scratch_pad()
    table = getattr(sp, 'symptom_validity_table')

    p = getattr(sp, 'data')

    if p['fever'] == ['fever_measure', 'fever_periodic'] and \
    p['body_pain'] == [['body_pain_area', 'body_pain_area_more_pain']]:
        print "PASS1"

    if sp.query('fever') == ['fever_measure', 'fever_periodic']:
        print "PASS2"

    if sp.query('fever', True) is None:
        print "PASS3"

    sp.set_top_level('fever')
    if sp.query('fever', True) == True:
        print "PASS4"

    sp.pop('fever')
    if sp.query('fever_measure') == True and sp.query('fever_periodic') is None \
    and sp.query('fever') == ['fever_periodic']:
        print "PASS5"

    sp.pop_specific(['fever', 'fever_measure'])
    if sp.query('fever_periodic') == True and sp.query('fever') == []:
        print "PASS6"

    # sp.set('joint_pain_area')
    # sp.set('joint_pain')
    # d = getattr(sp, 'data')
