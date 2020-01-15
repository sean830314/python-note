class Invoker:
    def __init__(self):
        self.commands = []

    def addCommand(self, cmd):
        self.commands.append(cmd)

    def cancelCommand(self, cmd):
        self.commands.remove(cmd)

    def invoke(self):
        for cmd in self.commands:
            cmd.execute()