import unittest
import Context
"""
需求描述

Amy(PO):

    As a 提需求單的使用者
    I want 需求單管理系統支援在某個需求的狀態改變時，記錄時間並以Email通知同仁
    So that 任何人可以輕易的識別目前需求的狀態

思考設計

JB:
我想可以透過一個switch來判斷某個需求目前的狀態，然後執行對應的作業。

Hachi:
恩，不過依照我們在Day5.Chain of Responsibility 職責鍊模式的經驗，用switch可能不是個好主意。
我們需要設定一個可以在每個狀態流動的模型，然後依照每個狀態去執行對應的動作。

Lily:
我們可以使用狀態模式(State)來實作這個需求，避免多重判斷和作業的程式碼。

JB::
聽起來不錯! 不過職責鍊也可以解決這個問題吧...!? 他們有何不同呢？

Lily:
我們先用狀態模式實作這個需求，然後我們再討論這兩種模式的使用時機。
定義

    實作每個狀態的對應類別，當對象的狀態改變時，透過這些狀態類別定義的方法來執行對應的策略。(WIKI)

實作狀態模式的方式：

    建立每一種狀態的類別，它們定義了該狀態下要做那些事，以及決定下一個狀態。
    建立存放狀態的對象(Context)，它具有改變狀態的權力。


State vs Chain of Responsibility

狀態模式和職責鏈模式都可以解決有順序、多重判斷=>執行邏輯的問題，例如IF ELSE，SWITCH CASE。
但兩者運作的方式不同：

    State(狀態模式)
        由對象(Context)控制何時轉換狀態及執行該狀態下的工作。
        對像透過已定義好的順序，往前或往後轉換狀態。

    Chain of Responsibility(職責鏈模式)
        對象只能決定何時發起鏈上的第一個點(Handler)，鏈上其他的點接續完成作業。
        對像能在開始作業前，改變職責鏈的順序。

"""

class UtState(unittest.TestCase):

    def test_state(self):
        expectedFinalState = "Done(已完成)"
        actualFinalState = ""

        context = Context.Context()
        while (context.currentState != None):
            actualFinalState = str(context.currentState)
            print("需求目前狀態=" + actualFinalState)
            context.action()
            
        self.assertEqual(actualFinalState, expectedFinalState)

    def test_state_actionback(self):
        expectedFinalState = "Working(進行中)"
        actualFinalState = ""

        context = Context.Context()
        hasDefect = False
        while (context.currentState != None):
            actualFinalState = str(context.currentState)
            print("需求目前狀態=" + actualFinalState)
            if hasDefect:
                break
            if actualFinalState == "Testing(測試中)":
                context.actionBack()
                hasDefect = True
            else:
                context.action()
            
        self.assertEqual(actualFinalState, expectedFinalState)



if __name__ == '__main__':
    unittest.main()