import unittest
from LoanColleague import LoanColleague
from OptionColleague import OptionColleague
from CreditColleague import CreditColleague
from MediatorWeight import MediatorWeight
from MediatorAverage import MediatorAverage

"""
需求描述

Amy(PO):

    As a 銀行行員
    I want 計算客戶評分時，可採用:

        各金融商品之評分模型但分別給與權重
        各金融商品之評分模型，加總後作平均

    So that 參考各模組之評分，達到KYC客戶風險評估之目的

思考設計

Hachi:
我們已經有各金融商品之評分模型，我們只要在每個金融商品建立一個評分方法，然後利用這些評分模組來計算分數即可。

JB:
聽起來我們需要在每一個金融商品再多加兩個方法，一個是權重計分，一個是平均總分! 那可得花一些時間!

Lily:;
而且會太依賴於其他金融商品的評分模型，我們來建立一個中介者來幫所有金融產品計算客戶分數如何？

JB:
讓一個人負責當窗口的概念嗎，聽起來不錯! 如果分數不正確的話，至少我們可以先找那個負責的窗口(笑)。
定義

    定義一個封裝了各組互動的對象的中介者，使這些對象避免明確直接引用來解除耦合度，並且可以獨立地改變他們的互動的方式。(WIKI)


在中介者模式(Mediator)中定義兩種角色(各自需建立抽象及實作類別):

    Colleague : 合作的對象，並且透過Mediator與其他對像溝通
    Mediator : 中介者，他知道所有合作的對象，並且協調這些對像協同作業

主程式如何應用中介者模式：
    找到該對像的中介者 (需要很多人幫忙時，先找這個專案負責人)
    請中介者發出執行的命令，協調大家開始作業 (專案負責人知道這件事需要哪些人幫忙，請他們一起進來協助作業)

"""
class UtMediator(unittest.TestCase):

    def test_weight_score(self):

        weightsForOption = [0.2, 0.5, 0.8]
        weightsForCredit = [0.1, 0.3, 0.2]
        weightsForLoan = [0.6, 0.2, 0]

        expectedOptionScore = (OptionColleague()).score() * weightsForOption[0] + (CreditColleague()).score() * weightsForOption[1] + (LoanColleague()).score() * weightsForOption[2]

        expectedCreditScore = (OptionColleague()).score() * weightsForCredit[0] + (CreditColleague()).score() * weightsForCredit[1] + (LoanColleague()).score() * weightsForCredit[2]

        expectedLoanScore = (OptionColleague()).score() * weightsForLoan[0] + (CreditColleague()).score() * weightsForLoan[1] + (LoanColleague()).score() * weightsForLoan[2]

        # Mediator for Option
        mediatorForOption = MediatorWeight(
            weightsForOption[0], weightsForOption[1], weightsForOption[2])
        option = OptionColleague()
        option.mediator = mediatorForOption
        actualOptionScore = option.mediator.score()  # Score!
        print("{0} 權重計分結果={1}".format(option.prod, actualOptionScore))

        self.assertEqual(actualOptionScore,  expectedOptionScore)

        # Mediator for Credit
        mediatorForCredit = MediatorWeight(
            weightsForCredit[0], weightsForCredit[1], weightsForCredit[2])
        option = CreditColleague()
        option.mediator = mediatorForCredit
        actualCreditScore = option.mediator.score()  # Score!
        print("{0} 權重計分結果={1}".format(option.prod, actualCreditScore))

        self.assertEqual(actualCreditScore,  expectedCreditScore)
 
        # Mediator for Loan
        mediatorForLoan = MediatorWeight(
            weightsForLoan[0], weightsForLoan[1], weightsForLoan[2])
        option = LoanColleague()
        option.mediator = mediatorForLoan
        actualLoanScore = option.mediator.score()  # Score!
        print("{0} 權重計分結果={1}".format(option.prod, actualLoanScore))

        self.assertEqual(actualLoanScore,  expectedLoanScore)
    
    def test_average_score(self):
        expectedLoanScore = ((OptionColleague()).score() + (CreditColleague()).score() + (LoanColleague()).score())/3

        mediator = MediatorAverage()
        loan = LoanColleague()
        loan.mediator = mediator
        actualLoanScore = loan.mediator.score()

        print("{0} 平均計分結果={1}".format(loan.prod, actualLoanScore))
        self.assertEqual(actualLoanScore,  expectedLoanScore)


if __name__ == '__main__':
    unittest.main()