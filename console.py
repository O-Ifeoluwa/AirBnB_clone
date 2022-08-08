#!/usr/bin/python3
"""program enters the entry point of the command interpreter"""
import cmd
from models import BaseModel


class HBNBCommand(cmd.Cmd):
    """entry point"""
    prompt = '(hbnb)'

    def do_quit(self,arg):
        """quit command to quit the console"""
        return True

    def help_quit(self):
        """help on quit event"""
        print('end-of-file: exit the program\n')

    def do_EOF(self, arg):
        """Quits the console"""
        return True

    def help_EOF(self):
        """Help on exit event"""
        print("end-of-file: exit the program\n")

    def emptyline(self):
        '''handles an empty line event'''
        return False

    def do_create(self, C_name):
        """
        creates a new instance of BaseModel, saves to
        JSON file and prints id
        """
        if C_name == '':
            print('**class name missing**')
        elif C_name not in HBNBCommand.classes.keys():
            print('**class doesn\'t exist**')
        else:
            new = HBNBCommand.classes[C_name]()
            new.save()
            print(new.id)

    def do_show(self, C_name):
        '''
        prints the string representation of an instance
        based in the class name and id
        '''
        split_list = C_name.split()
        if split_name =='':
            print('**class name missing**')
            return
        elif split_name[0] not in HBNBCommand.classes.keys():
            print('**class doesn\'t exist**')
        else:
            instances = models.storage.all()
            keys = split_list[0] + '.' + split_list[1]
            if keys in instances:
                print(instances[keys])
            else:
                print('**no instance found**')

    def do_destroy(self, C_name):
        '''
        deletes an instance based on the class name and id
        saves the change into the JSON file
        '''
        class_name = C_name.split()

        if class_name = '':
            print('**class name missing**')
        elif C_name [0] not in HBNBCommand.classes.keys():
            print('**class name doesn\'t exist**')
        elif len(class_name) == 0:
            print('**instance id missing**')
        else:
            instances = class_name[0] + '.' + class_name[1]
            if instances in models.storage.all():
                del models.storage.all()[instances]
                models.storage.save()
            else:
                print('** no instance found **')


    if __name__ == '__main__':
        HBNBCommand().cmdloop()
