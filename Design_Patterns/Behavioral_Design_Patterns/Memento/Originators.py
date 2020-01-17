import uuid
import copy
from abc import ABC, abstractmethod
from Mementos import Memento, EflowMemento
"""

Originator

Originator是主程式操作的對像，它擁有需要被記錄的資料，並且提供以下功能

    建立備忘錄(不是儲存喔!)
    將目前資料回復成任何一張備忘錄裡的狀態

"""
class Originator(ABC):
    @abstractmethod
    def createMemento(self):
        pass

    @abstractmethod
    def restoreMemento(self, memento= Memento):
        pass

class EflowOriginator(Originator):
    def __init__(self):
        self.eflow = None
    
    def createMemento(self):
        uid = str(uuid.uuid4())
        memento = EflowMemento(uid, copy.deepcopy(self.eflow))
        return memento

    def restoreMemento(self,memento=Memento):
        self.eflow = memento.eflow