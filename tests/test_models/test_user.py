#!/usr/bin/python3
'''
mod def
'''
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    '''
    class def
    '''

    def test_moduleDocs(self):
        '''
        mod
        '''
        moduleDoc = (
                __import__("models.user")
                .user.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        class
        '''
        classDoc = (
                __import__("models.user")
                .user.User.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_attributes_Type(self):
        '''
        email password,frist na last name
        '''
        user = User()
        self.assertIs(type(user.email), str)
        self.assertIs(type(user.password), str)
        self.assertIs(type(user.first_name), str)
        self.assertIs(type(user.last_name), str)


if __name__ == "__main__":
    unittest.main()
