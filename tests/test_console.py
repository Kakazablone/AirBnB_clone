import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from models.engine.file_storage import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        '''Set up the test environment'''
        self.cmd = HBNBCommand()
        models.storage.classes = {}  # Reset classes before each test

    def test_create_success(self):
        '''Test the successful creation of an instance'''
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd('create BaseModel')
            output = mock_stdout.getvalue().strip()
            self.assertIn('id', output)

    def test_create_missing_class(self):
        '''Test handling the case where class name is missing during create'''
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd('create')
            output = mock_stdout.getvalue().strip()
            self.assertIn('** class name missing **', output)

    def test_create_nonexistent_class(self):
        '''Test handling the case where the specified class doesn't exist during create'''
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd('create InvalidClass')
            output = mock_stdout.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_all_no_class(self):
        '''Test the 'all' command without specifying a class'''
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd('all')
            output = mock_stdout.getvalue().strip()
            self.assertNotIn('** class doesn\'t exist **', output)

    def test_all_nonexistent_class(self):
        '''Test handling the case where the specified class for 'all' doesn't exist'''
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd('all InvalidClass')
            output = mock_stdout.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_emptyline(self):
        '''Test handling an empty command line'''
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd('')
            output = mock_stdout.getvalue().strip()
            self.assertEqual('', output)

    def test_do_EOF(self):
        '''Test handling the 'EOF' command'''
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.cmd.onecmd('EOF'))

    def test_do_quit(self):
        '''Test handling the 'quit' command'''
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.cmd.onecmd('quit'))

    def test_nonexistent_command(self):
        '''Test handling an unknown command'''
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd('nonexistent_command')
            output = mock_stdout.getvalue().strip()
            self.assertIn('*** Unknown syntax', output)

    def test_invalid_update_command(self):
        '''Test handling an invalid 'update' command'''
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd('update')
            output = mock_stdout.getvalue().strip()
            self.assertIn('** class name missing **', output)

    def test_invalid_update_attribute(self):
        '''Test handling an invalid 'update' command without an instance id'''
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd('update BaseModel')
            output = mock_stdout.getvalue().strip()
            self.assertIn('** instance id missing **', output)

    def test_invalid_update_value(self):
        '''Test handling an invalid 'update' command without an attribute name'''
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd('update BaseModel 1')
            output = mock_stdout.getvalue().strip()
            self.assertIn('** attribute name missing **', output)

    def test_update_missing_value(self):
        '''Test handling an 'update' command without specifying a value'''
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd('update BaseModel 1 attribute')
            output = mock_stdout.getvalue().strip()
            self.assertIn('** value missing **', output)

if __name__ == '__main__':
    unittest.main()

