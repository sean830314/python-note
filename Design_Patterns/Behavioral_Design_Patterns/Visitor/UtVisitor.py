import unittest
from decimal import Decimal,getcontext
import Elements
from Visitors import VisitorDiscount4Count, VisitorDiscount4TotalPrice
from ObjectStructure import ObjectStructure
"""
需求描述
Amy(PO):

As a 電商老闆
I want 舉辦行銷活動，購物車結帳時：

書籍雜誌：會員相同類別10本以上八折優惠
生活用品：會員相同品項$1,000以上九折優惠
So that 提高網站轉換率及營收
思考設計
JB:
這個需求看起來很簡單，但是仔細想了一下，發現要寫好程式很困難耶! 我們得考慮：

既有的優惠條件會不會改變?
會不會未來再新增其他商品的優惠？
Lily:
你說的沒錯，唯一不變的就是"變"。
所以我們得把這些折扣的算法轉換成策略模式(Strategy)；這個可以解決第一個問題。
第二個問題，我們得把相同優惠策略的商品放在一個抽象的容器，結帳時，把在相同集合的不同商品採用一樣的優惠策略計算最後的價錢，未來如果有其他商品需要用到現成的優惠，就可以把它也丟到這個抽象的容器即可!

JB:
聽起來好像將某一個容器裡面的所有元素，讓他們跑同一個策略？

Lily:
沒錯! 這種行為(Behavioral design patterns)叫做Visitor訪問者模式!

定義
表示要在結構裡面的元素執行的操作。訪問者(Visitor)可以讓你定義一個新的操作讓這些元素使用，而不用改變元素類別。 (WIKI)

簡單的來說! 訪問者模式(Visitor)是策略模式(Strategy)的延伸。
在策略模式中，我們只讓一個對象執行注入的策略。
但在訪問者模式，我們可以讓很多對象依序執行注入的策略。
先有這個概念之後，我們來看例子，最後再討論兩者使用的時機。

Element : 可存放要處理的物件或參數，再由外部帶入一個Visitor。 處理的方法是實作在Visitor。
ObjectStructure：存放Element集合，提供新增、刪除元素，以及讓Client呼叫處理元素的方法。
Visitor：提供方法注入於Element中做處理。


Visitor vs. Strategy
我們來看了解一下兩者的使用時機：

Strategy 是設計來對一個物件 注入不同處理邏輯。
Visitor 是設計來對多個物件 注入處理邏輯， 當然也可以對單一個物件注入不同處理邏輯。
Strategy 簡單，適用於多數場合。
Visitor 本身使用了 Strategy的概念。
Visitor 適用於有多個實作類別或是子類別，而且每個類別需要特別的處理邏輯。
"""

class UtVisitor(unittest.TestCase):

    _shopcart = None

    def __init__(self, *args, **kwargs):
        super(UtVisitor, self).__init__(*args, **kwargs)
        self._shopcart = [
            Elements.Product(productType=Elements.ProductTypeEnum.Book,
                             name="設計模式的解析與活用", unitPrice=480, amount=20),
            Elements.Product(productType=Elements.ProductTypeEnum.Book,
                             name="使用者故事對照", unitPrice=580, amount=5),
            Elements.Product(productType=Elements.ProductTypeEnum.Living,
                             name="吸塵器", unitPrice=2000, amount=2),
            Elements.Product(productType=Elements.ProductTypeEnum.Living,
                             name="毛巾", unitPrice=50, amount=10),
            Elements.Product(productType=Elements.ProductTypeEnum.Electronic,
                             name="Surface Pro", unitPrice=50000, amount=2)
        ]
    
    def test_visitorDiscount4Amount(self):
        # getcontext().prec = 2
        
        expected = self._shopcart[0].unitPrice * Decimal(self._shopcart[0].amount) * Decimal(0.8) + self._shopcart[1].unitPrice * Decimal(self._shopcart[1].amount)
        actual = 0

        checkout = ObjectStructure()

        # Attach the elements into ObjectStructure
        targetProds = [
            x for x in self._shopcart if x.productType == Elements.ProductTypeEnum.Book]
        for item in targetProds:
            checkout.attach(item)

        # Accept all the elements and execute the strategy from certain Visitor
        checkout.accept(VisitorDiscount4Count())

        for item in checkout.elements:
            actual = actual + item.totalPrice

        self.assertEqual(actual, expected)
    
    def test_visitorDiscount4TotalPrice(self):
        # getcontext().prec = 2

        # expected = float(self._shopcart[2].unitPrice) * float(self._shopcart[2].amount) * float(0.9) + float(self._shopcart[3].unitPrice) * float(self._shopcart[3].amount)
        expected = self._shopcart[2].unitPrice * Decimal(self._shopcart[2].amount) * Decimal(0.9) + self._shopcart[3].unitPrice * Decimal(self._shopcart[3].amount)        
        actual = 0

        checkout = ObjectStructure()

        # Attach the elements into ObjectStructure
        targetProds = [
            x for x in self._shopcart if x.productType == Elements.ProductTypeEnum.Living]
        for item in targetProds:
            checkout.attach(item)

        # Accept all the elements and execute the strategy from certain Visitor
        checkout.accept(VisitorDiscount4TotalPrice())

        for item in checkout.elements:
            actual = actual + item.totalPrice

        self.assertEqual(actual, expected)
    

if __name__ == '__main__':
    unittest.main()