import unittest
import datetime
from Memento_models import Eflow
from Mementos import Memento,EflowMemento
from Originators import Originator, EflowOriginator
from Caretaker import Caretaker
"""
需求描述

Amy(PO):

    As a 電子表單使用者
    I want 系統可以在我填寫表單時，提供記錄草稿的功能，儲存該張表單後，即刪除該單所有草稿，但若未儲存，則須保留草稿
    So that 避免臨時無法完成表單而造成已填寫之資料遺失情況

思考設計

JB:
(打哈欠)這個User Story有點長，我總是記不住，我得重頭再看一次...

Lily:
你得有充足的睡眠! 避免像個鐵人一樣在半夜寫程式或寫文章! 好了，我建議用備忘錄解決這件事。

JB:
你說的沒錯，把一些重要的東西記在備忘錄，需要的時候就拿出來看...

Lily:
喔，我是指用設計模式:Memento，來解決這個Backlog，它提供了可以隨時儲存現在的狀態，和回復之前的狀態的行為模式。

定義

    在不違反封裝的原則下，取得一個物件的內部狀態並保留在外部，並提供對象恢復到其以前的狀態的能力 (WIKI)

在Memento中，定義了以下角色：

    Originator: 擁有要被儲存的資料
    Memento: State(可以是物件、標記、或其他內容)
    Caretaker(管理人): 管理與儲存Memento(由Originator提供)，提供存取的介面



執行結果：

儲存一張表單! 建立日期2018/01/06 18:46:55，內容: 簽呈：工程師Hachi申請加薪$3,000!
儲存一張表單! 建立日期2018/01/06 18:48:55，內容: 簽呈：工程師Hachi申請加薪$30!
回存一張表單! 建立日期2018/01/06 18:46:55，內容: 簽呈：工程師Hachi申請加薪$3,000!
"""
class UtMemento(unittest.TestCase):

    def test_memento(self):
        caretaker = Caretaker()
            
        originator = EflowOriginator()
        originator.eflow = Eflow(
                createOn = datetime.datetime.now(), 
                formData = "簽呈：工程師Hachi申請加薪$3,000!")

        # 第一次建立備忘
        memento = originator.createMemento() 
        # 第一次儲存備忘
        caretaker.add("Hachi的新年新希望" , memento)
            
        # 老闆收到表單，找Hachi約談並施展三寸不爛之舌，只同意加薪$30
        originator.eflow.createOn = originator.eflow.createOn + datetime.timedelta(0,2)
        originator.eflow.formData = "簽呈：工程師Hachi申請加薪$30!" 

        # 第二次建立備忘
        memento = originator.createMemento()
        # 第二次儲存備忘
        caretaker.add("Hachi的新年新希望v2" , memento)

        # 有新公司找Hachi過去，Hachi準備提離職，老闆趕緊同意先前條件
        # Hachi調出之前該單的備忘回存
        mementoOld = caretaker.get("Hachi的新年新希望")
        originator.restoreMemento(mementoOld)

        self.assertEqual(originator.eflow.formData,  "簽呈：工程師Hachi申請加薪$3,000!")


if __name__ == '__main__':
    unittest.main()