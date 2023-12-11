#!/usr/bin/python3
'''
mod def
'''
import unittest
from models.engine.file_storage import FileStorage
from uuid import UUID
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    '''
    class
    '''

    def test_moduleDocs(self):
        '''
        mod
        '''
        moduleDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        class
        '''
        classDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_methodDocsSave(self):
        '''
        method
        '''
        methodDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.save.__doc__)
        self.assertGreater(len(methodDoc), 0)


if __name__ == "__main__":
    unittest.main()
