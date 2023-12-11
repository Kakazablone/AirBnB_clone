#!/usr/bin/python3
'''
mod def
'''
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''
    class
    '''

    def test_moduleDocs(self):
        '''
        mod
        '''
        moduleDoc = (
                __import__("models.review")
                .review.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        class
        '''
        classDoc = (
                __import__("models.review")
                .review.Review.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_attributes_Type(self):
        '''
        text,place id
        '''
        review = Review()
        self.assertIs(type(review.text), str)
        self.assertIs(type(review.place_id), str)
        self.assertIs(type(review.user_id), str)


if __name__ == "__main__":
    unittest.main()
