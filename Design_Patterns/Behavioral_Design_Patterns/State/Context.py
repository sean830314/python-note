import States
"""
Context

由State的程式碼，我們得知在每一次Context開始作業(Action())時，必須把它自己作為參數丟給當下狀態對應的State類別，再由State類別去做事以及更新Context最新的狀態。
"""


class Context:
    
    def __init__(self):
        self.currentState = States.StateToDo()

    def action(self):
        self.currentState.action(self)
        
    def actionBack(self):
        self.currentState.actionBack(self)