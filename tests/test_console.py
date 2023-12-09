import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_do_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.do_EOF(""))
            self.assertEqual(f.getvalue(), "\n")

    def test_do_quit(self):
        self.assertTrue(self.console.do_quit(""))

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.emptyline()
            self.assertEqual(f.getvalue(), "")

    def test_do_create_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_create("")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_do_create_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_create("InvalidClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_do_create_valid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_create("BaseModel")
            self.assertIn("created", f.getvalue())

    def test_do_show_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_show("")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_do_show_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_show("InvalidClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_do_show_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_show("BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_do_show_valid_class_name_and_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_show("BaseModel 123")
            self.assertIn("** no instance found **", f.getvalue())

    def test_do_destroy_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_destroy("")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_do_destroy_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_destroy("InvalidClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_do_destroy_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_destroy("BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_do_destroy_valid_class_name_and_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_destroy("BaseModel 123")
            self.assertIn("** no instance found **", f.getvalue())

    def test_do_all_no_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_all("")
            self.assertIn("** class doesn't exist **", f.getvalue())

    def test_do_all_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_all("InvalidClass")
            self.assertIn("** class doesn't exist **", f.getvalue())

    def test_do_all_valid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_all("BaseModel")
            self.assertEqual(f.getvalue(), "[]\n")

    def test_do_update_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_update("")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_do_update_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_update("InvalidClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_do_update_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_update("BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_do_update_valid_class_name_and_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_update("BaseModel 123")
            self.assertIn("** no instance found **", f.getvalue())

    def test_precmd(self):
        formatted_args = self.console.precmd("create(BaseModel, {'name': 'test', 'value': 10})")
        self.assertEqual(formatted_args, "create BaseModel  {'name': 'test', 'value': 10}")

if __name__ == '__main__':
    unittest.main()
