#!/usr/bin/python3
'''
mod def
'''
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    '''
    class def
    '''

    def test_moduleDocs(self):
        '''
        module
        '''
        moduleDoc = (
                __import__("models.city")
                .city.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        class do
        '''
        classDoc = (
                __import__("models.city")
                .city.City.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_name_Type(self):
        '''
        name
        '''
        city = City()
        self.assertIs(type(city.name), str)

    def test_state_id_Type(self):
        '''
        state
        '''
        city = City()
        self.assertIs(type(city.state_id), str)


if __name__ == "__main__":
    unittest.main()
