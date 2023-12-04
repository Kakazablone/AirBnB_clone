The Airbnb project is a clone of the Airbnb website. The first part is the console version which expects us to learn how to use the cmd python module to interact with our models.
The Command interpreter created with cmd uses a loop to read all lines from its input, parse them and then dispatch the command to an appropriate command handler.
The input lines are parsed into two parts; the command and any other text on the line.
Note that the end of file marker is dispachted to do_EOF(). If a command handler returns a true value, the program will exit cleanly.
EXAMPLE
import cmd
class Samba(cmd.Cmd):

    def do_Stephen(self, line):
        print("Mambo")
    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    Samba().cmdloop()
All methods MUSt start with the do_ statement. You can use a different prompt and your documentation should capture  the various help scenarios.
