from abc import ABC, abstractmethod
class BaseLogger(ABC):
    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def warn(self):
        pass

    @abstractmethod
    def error(self):
        pass

class TextLogger(BaseLogger):
    def debug(self,msg):
        print("(Text)Debug: " + msg)

    def warn(self,msg):
        print("(Text)Warn: " + msg)

    def error(self,msg):
        print("(Text)Error: " + msg)
          

class DbLogger(BaseLogger):
    def debug(self,msg):
        print("(Database)Debug: " + msg)

    def warn(self,msg):
        print("(Database)Warn: " + msg)

    def error(self,msg):
        print("(Database)Error: " + msg)