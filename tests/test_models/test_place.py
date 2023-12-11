#!/usr/bin/python3
'''
mod def
'''
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    '''
    class def
    '''

    def test_moduleDocs(self):
        '''
        mod
        '''
        moduleDoc = (
                __import__("models.place")
                .place.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        class
        '''
        classDoc = (
                __import__("models.place")
                .place.Place.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_attributes_Type(self):
        '''
        attribute
        '''
        place = Place()
        self.assertIs(type(place.name), str)
        self.assertIs(type(place.city_id), str)
        self.assertIs(type(place.user_id), str)
        self.assertIs(type(place.description), str)
        self.assertIs(type(place.number_rooms), int)
        self.assertIs(type(place.number_bathrooms), int)
        self.assertIs(type(place.max_guest), int)
        self.assertIs(type(place.price_by_night), int)
        self.assertIs(type(place.latitude), float)
        self.assertIs(type(place.longitude), float)
        self.assertIs(type(place.amenity_ids), str)


if __name__ == "__main__":
    unittest.main()
