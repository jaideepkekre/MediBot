#!usr/bin/python
# Owner : @v0dro
# _author_ =  @v0dro
# _info_   = Table which stores state of symptoms

class symptom_validity_table(object):
    """
    This class maintains a table that contains the state of each symptom.

    Each symptom tag is stored with its respective state:
    {
        'fever' : None,
        'fever_periodic' : None,
        # ....
    }


    Score is to be only used by buckets to set the score for each symptom
    """
    def __init__(self):
        self.data = dict()

        top_tags = __import__('top_questions').data().keys()

        for top_tag in top_tags:
            self.data[top_tag] = None
            sub_tags_data_dict = __import__(top_tag).data()

            for sub_tag, sub_tag_data in sub_tags_data_dict.iteritems():
                self.data[sub_tag] = None

                while sub_tag_data.has_key('linked_questions'):
                    sub_tag_data = sub_tag_data['linked_questions']
                    linked_tag = sub_tag_data['tag']
                    self.data[linked_tag] = None
        self.score = dict(self.data)
        for symptom in self.score.keys():
            self.score[symptom]=0

    def get_dict(self):
        return self.data

    def set(self, tag, value=True):
        if self.data.has_key(tag):
            self.data[tag] = value
        else:
            raise AttributeError("Non existent key " + tag)

    def get(self, tag):
        return self.data[tag]

    def print_score(self):
        print self.score

    def set_score(self, tag, value=0):
        if self.score.has_key(tag):
            self.score[tag] = value
        else:
            raise AttributeError("Non existent key " + tag)

    def get_score(self, tag):
        return self.score[tag]

    """
    Subtract one symptom_validity_table from another to get the diff as a list.
    """
    def __sub__(self, other):
        d = getattr(other, 'data')
        tags = list()

        for tag in d:
            if not (self.data[tag] is None and d[tag] is None):
                tags.append(tag)

        return tags

if __name__ == '__main__':
    import unittest

    class TestSymptomTable(unittest.TestCase):
        def test_symptom_table(self):
            t = symptom_validity_table()
            data = getattr(t, 'data')

            self.assertEqual(data['fever'], None)
            self.assertEqual(data['body_pain'], None)
            self.assertEqual(data['fever_periodic'], None)
            self.assertEqual(data['body_pain_area_more_pain'], None)

            t.set('fever')
            self.assertEqual(data['fever'], True)

            t.set('body_pain_area_more_pain')
            self.assertEqual(data['body_pain_area_more_pain'], True)

            t.set('body_pain', False)
            self.assertEqual(data['body_pain'], False)

            f = symptom_validity_table()

            diff = t - f
            self.assertEqual(diff, ['fever', 'body_pain', 'body_pain_area_more_pain'])

    unittest.main()
