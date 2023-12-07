import unittest
from models import storage
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_instance_creation(self):
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, 'id'))
        self.assertTrue(hasattr(instance, 'created_at'))
        self.assertTrue(hasattr(instance, 'updated_at'))
        self.assertTrue(isinstance(instance.id, str))
        self.assertTrue(isinstance(instance.created_at, datetime))
        self.assertTrue(isinstance(instance.updated_at, datetime))

    def test_str_representation(self):
        instance = BaseModel()
        string_representation = str(instance)
        self.assertIn(instance.id, string_representation)
        self.assertIn(str(type(instance).__name__), string_representation)

    def test_save_method(self):
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        new_updated_at = instance.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIn('__class__', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)

    def test_deserialization_from_dict(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        new_instance = BaseModel(**instance_dict)
        self.assertEqual(instance.id, new_instance.id)
        self.assertEqual(instance.created_at, new_instance.created_at)
        self.assertEqual(instance.updated_at, new_instance.updated_at)

if __name__ == '__main__':
    unittest.main()
