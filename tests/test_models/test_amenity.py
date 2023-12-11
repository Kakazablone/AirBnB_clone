#!/usr/bin/python3
'''
mod def
'''
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''
    class def
    '''

    def test_moduleDocs(self):
        '''
        test ya module
        '''
        moduleDoc = (
                __import__("models.amenity")
                .amenity.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        test ya class
        '''
        classDoc = (
                __import__("models.amenity")
                .amenity.Amenity.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_name_Type(self):
        '''
        test ya name 
        '''
        amenity = Amenity()
        self.assertIs(type(amenity.name), str)


if __name__ == "__main__":
    unittest.main()
