"""
Command Pattern adds a level of abstraction between actions and includes an object, which invokes these actions.

In this design pattern, client creates a command object that includes a list of commands to be executed. 
The command object created implements a specific interface.

Following is the basic architecture of the command pattern −


Explanation

The output implements all the commands and keywords listed in Python language. It prints the necessary values of the variables.
"""


def demo(a, b, c):
    print('a:', a)
    print('b:', b)
    print('c:', c)


class Command:
    def __init__(self, cmd, *args):
        self._cmd = cmd
        self._args = args

    def __call__(self, *args):
        return self._cmd(*self._args + args)


cmd = Command(dir, __builtins__)
print(cmd())
cmd = Command(demo, 1, 2)
cmd(3)