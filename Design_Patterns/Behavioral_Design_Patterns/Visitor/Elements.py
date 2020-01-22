from abc import ABC, abstractmethod
from enum import Enum
from decimal import Decimal
"""
Element
在這個例子，Element很明顯的就是我們放在購物車的商品，
其屬性應包含商品名稱、種類、單價、數量以及我們要計算的總價格，以及一個可以讓Visitor執行訪問的方法：Accept。
"""
class ProductTypeEnum(Enum):
    Book = 1,  # 書
    Living = 2,  # 生活用品
    Electronic = 3  # 電子用品


class Element(ABC):
    def __init__(self, productType: ProductTypeEnum, name="", unitPrice=0, amount=0):
        self.productType = productType
        self.name = name
        self.unitPrice = Decimal(unitPrice)
        self.amount = amount
        self.totalPrice=Decimal(0)

    @abstractmethod
    def accept(self, visitor):
        pass


class Product(Element):
    def __init__(self, productType=ProductTypeEnum, name="", unitPrice=0, amount=0):
        super().__init__(productType, name, unitPrice, amount)

    def accept(self, visitor):
        visitor.visit(self)