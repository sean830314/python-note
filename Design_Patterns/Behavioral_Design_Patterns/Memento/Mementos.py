from abc import ABC, abstractmethod
from Memento_models import Eflow
"""
Memento

在這個例子，我們要放在備忘錄的目標是：電子表單，所以先建立如下之Model:

Memento即代表一份備忘錄，我們在這個備忘錄記錄我們想留存的東西；
以這個例子來看，我們要留存的是電子表單物件；為了區別每一份備忘錄，我們在備忘錄上也記錄一個唯一的序號(Id)。
"""
class Memento(ABC):
    def __init__(self, id=""):
        self.id = id

class EflowMemento(Memento):
    def __init__(self, id="", eflow=Eflow):
        self.id = id
        self.eflow = eflow