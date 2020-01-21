from abc import ABC, abstractmethod
import Context
"""
State

我們假設需求管理系統裡面的一項需求，具有以下四種狀態：

    TODO
    Working
    Testing
    Done
"""


class State(ABC):
    @abstractmethod
    def action(self,context=Context):
        pass
    
    @abstractmethod
    def actionBack(self,context=Context):
        pass


class StateToDo(State):
    def __str__(self):
        return "TODO(待做事項)"

    def action(self,context=Context):
        
        # Do something...

        # Set next state
        context.currentState = StateWorking()
        print("The requirement is on TODO list, send email to IT manager.");
    def actionBack(self, context=Context):
        pass
class StateWorking(State):
    def __str__(self):
        return "Working(進行中)"

    def action(self,context=Context):
        
        # Do something...

        # Set next state
        context.currentState = StateTesting()
        print("The requirement is completed, send email to users!");
    def actionBack(self, context=Context):
        pass

class StateTesting(State):
    def __str__(self):
        return "Testing(測試中)"

    def action(self,context=Context):
        
        # Do something...

        # Set next state
        context.currentState = StateDone()
        print("Test ok, send email to operation team!");
    def actionBack(self,context=Context):
        
        # Do something...

        # Set next state
        context.currentState = StateWorking()
        print("Test NG, send email to development team!");
class StateDone(State):
    def __str__(self):
        return "Done(已完成)"

    def action(self,context=Context):
        
        # Do something...

        # Set next state
        context.currentState = None
        print("Close the requirement, send email to all stakeholders!");
    def actionBack(self, context=Context):
        pass