import Elements
import Visitors
"""
Element
在這個例子，Element很明顯的就是我們放在購物車的商品，
其屬性應包含商品名稱、種類、單價、數量以及我們要計算的總價格，以及一個可以讓Visitor執行訪問的方法：Accept。
"""

class ObjectStructure:
    def __init__(self):
        self.elements = []

    def attach(self,element: Elements.Element):
        self.elements.append(element)

    def detach(self,element: Elements.Element):
        self.elements.remove(element)

    def accept(self,visitor: Visitors.Visitor):
        for elm in self.elements:
            elm.accept(visitor)