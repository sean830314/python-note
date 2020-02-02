import unittest
from TrfFixing import TrfFixing
from DkoFixing import DkoFixing
"""
定義

    定義一個包含方法和執行流程的抽象樣板，讓實作類別透過繼承的方式實作方法的細節，最後透過樣板已經定義好的流程執行任務。(WIKI)

我們建立一個抽象的Template，裡面包含了比價流程每個步驟會用到的方法，以及如何利用這些方法進行比價的流程。


    樣板方法的優缺點如下：

        優點：符合OCP，易於維護
        缺點：流程(步驟)寫在父類別，但是邏輯寫在子類別，造成程式碼不易閱讀


"""

class UtTemplate(unittest.TestCase):

    def test_template(self):
        trfFixing = TrfFixing()
        trfFixing.fixing()

        dkoFixing = DkoFixing()
        dkoFixing.fixing()

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()