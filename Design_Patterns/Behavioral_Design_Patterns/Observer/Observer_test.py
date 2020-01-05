

from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update(self,absence:str, designee:str):
        pass

class ObserverPbx(Observer):

    def update(self,absence:str, designee:str):
        print("[PBX] 已指定轉接{0}的來電給{1}!".format(absence, designee))

class ObserverMailServer(Observer):

    def update(self,absence:str, designee:str):
        print("[Mail Server] 已設定將{0}的信副本給{1}!".format(absence, designee))

class Subject(ABC):

    def __init__(self):
        self.observers=[]

    @abstractmethod
    def attach(self,observer: Observer): 
        pass

    def detach(self,observer: Observer):
        pass

    def notify(self, absence:str, designee:str):
        pass

class SubjectEflow(Subject):

    def __init__(self):
        super().__init__()

    def attach(self,observer: Observer): 
        self.observers.append(observer)

    def detach(self,observer: Observer):
        self.observers.remove(observer)

    def notify(self, absence:str, designee:str):
        for observer in self.observers:
            observer.update(absence, designee)
if __name__ == '__main__':
    """
    定義
    定義對象之間的一對多依賴關係，當一個對象更改狀態時，會自動通知並更新其所有依賴的對象。

    Observer : 觀察者，必須有讓Subject可以Notify的方法。
    Subject：可以訂閱、取消訂閱Observer，並有Notify所有訂閱的Observer的方法。

    底下的範例，是在使用者申請一張請假單時，電子表單系統於請假日當天

    通知交換機自動指定轉接給代理人員
    通知Mail Server將收到的eMail副本給代理人員
    """
    # Create observers
    pbx = ObserverPbx()
    ms = ObserverMailServer()
        
    # Create subject
    subject = SubjectEflow()
    subject.attach(pbx)
    subject.attach(ms)

    # Notify when JB is leave of absence
    subject.notify("JB", "Hachi")