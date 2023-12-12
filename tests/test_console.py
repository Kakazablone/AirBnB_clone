#!/usr/bin/python3
'''
mod def
'''
import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


class TestConsole(unittest.TestCase):
    '''
    console
    '''
    def test_moduleDocs(self):
        '''
        mod
        '''
        moduleDoc = __import__("console").__doc__
        self.assertGreater(len(moduleDoc), 0)

    def test_ClassDocs(self):
        '''
        class
        '''
        classDoc = __import__("console").HBNBCommand.__doc__
        self.assertGreater(len(classDoc), 0)

    def test_quit(self):
        '''
        quit
        '''
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            expected_output = ""
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_EOF(self):
        '''
        end of file
        '''
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            expected_output = ""
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_help(self):
        '''
        help
        '''
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            expected_output = """Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update  update_list"""
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_create_BaseModel_success(self):
        '''
        create base
        '''
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            expected_output = 36
            self.assertEqual(expected_output, len(f.getvalue().strip()))

    def test_create_BaseModel_no_class_name(self):
        '''
        create b
        '''
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            expected_output = "** class name missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_create_BaseModel_wrong_class_name(self):
        '''
        create b
        '''
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create MyClass")
            expected_output = "** class doesn't exist **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_show_BaseModel_no_class_name(self):
        '''
        show b
        '''
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            expected_output = "** class name missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_show_BaseModel_wrong_class_name(self):
        '''
        show b
        '''
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show MyClass")
            expected_output = "** class doesn't exist **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_show_BaseModel_no_instance_id(self):
        '''
        show b
        '''
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            expected_output = "** instance id missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_show_BaseModel_instance_not_found(self):
        '''
        show
        '''
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 121212")
            expected_output = "** no instance found **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_BaseModel_no_class_name(self):
        '''
        d base
        '''
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            expected_output = "** class name missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_BaseModel_wrong_class_name(self):
        '''
        destroy
        '''
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyClass")
            expected_output = "** class doesn't exist **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_BaseModel_no_instance_id(self):
        '''
        destroy
        '''
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            expected_output = "** instance id missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_BaseModel_instance_not_found(self):
        '''
        destroy
        '''
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            expected_output = "** no instance found **"
            self.assertEqual(expected_output, f.getvalue().strip())

     def test_all_single_object_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())



if __name__ == "__main__":
    unittest.main()
