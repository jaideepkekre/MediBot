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
        pass

    """
    Send a list of tags and sub tags to check status.

    The tags listed in the list should be nested. If at the end of the traversal
    more nested dicts are detected, a list containing the names of sub-tags which
    have 'status' set to 'None' will be returned.

    Example:
        query(['fever'])
        # => ['fever_periodic', 'fever_measure']

        query(['fever', 'fever_periodic'])
        # => None
    """
    def query(self, tag_list):
        pass

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
        pass


if __name__ == '__main__':
    sp = scratch_pad()

    d = getattr(sp, 'data')
    if d['fever']['status'] == None and d['joint_pain']['joint_pain_area']['joint_pain_area_more_pain']['status'] == None:
        print "PASS"

    if sp.query(['fever']) == ['fever_periodic', 'fever_measure']:
        print "PASS"

    sp.set(['fever'])
    d = getattr(sp, 'data')
    
    if d['fever'] == True:
        print "PASS"

    sp.set(['joint_pain', 'joint_pain_area'])
    d = getattr(sp, 'data')

    if d['joint_pain']['status'] == True and d['joint_pain']['joint_pain_area'] == True:
        print "PASS"
