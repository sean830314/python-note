import sys
import os.path
from BaseLogger import DbLogger
from BaseLogger import TextLogger

class MyLogger:   
    def warn(self, msg):
        textLogger = TextLogger()
        dbLogger = DbLogger()
        textLogger.warn(msg)
        dbLogger.warn(msg)

    def read(self):
        print("(Database)Dump logs.")
        print("(Text)Dump logs.")