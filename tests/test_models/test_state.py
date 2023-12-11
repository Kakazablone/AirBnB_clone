#!/usr/bin/python3
'''
mod def
'''
import unittest
from models.state import State


class TestState(unittest.TestCase):
    '''
    class
    '''

    def test_moduleDocs(self):
        '''
        mod
        '''
        moduleDoc = (
                __import__("models.state")
                .state.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        class
        '''
        classDoc = (
                __import__("models.state")
                .state.State.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_name_Type(self):
        '''
        name
        '''
        state = State()
        self.assertIs(type(state.name), str)


if __name__ == "__main__":
    unittest.main()
