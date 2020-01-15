import unittest
from Receivers import ReceiverAirForce, ReceiverArmy, ReceiverNavy
from Commands import CmdBreakthrough, CmdDefense, CmdSupport
from Invoker import Invoker

"""
需求描述

Amy(PO):

    As a 銀行交易員
    I want 在衍生性金融商品管理系統可以自動比價
    So that 提供獲利及損失模型，讓客戶理解投資風險

思考設計

JB:
我們的系統目前支援TARF、DKO和Synthetic Forward，我和交易員談過，他們的比價流程是一樣的，但是邏輯不一樣。
問題是...我們怎麼開始？

Lily:
恩，我們可以先從建立一個標準的比價流程開始! 我們來用樣板方法(Template Method)設計一套比價範本給這些產品。
再來設計每種產品的類別並實作裡面的方法!

定義

    將請求封裝為物件，允許使用不同的請求來參數化客戶端，駐列或記錄這些請求，並支持可撤銷的操作 ((WIKI)[https://en.wikipedia.org/wiki/Command_pattern])


    Client: 總指揮官，負責
        建立命令
        將命令放到作戰計畫，或從作戰計畫移除
        執行作戰計畫

    Command: 命令
        每個命令對應一個Receiver(部隊指揮官)
        命令被執行時，觸發Receiver裡面的執行細節

    Receiver: 部隊指揮官
        負責提供命令如何執行的細節
        沒有主動執行細節的能力，而是藉由命令被執行才觸發

    Invoker: 作戰計畫，提供
        儲放或取消命令
        當收到Client(總指揮官)執行的通知，執行所有內部的命令


Receiver

我們定義部隊的指揮官為三種：

    ReceiverArmy : 陸軍
    ReceiverNavy : 海軍
    ReceiverAirForce : 空軍


Command

每個命令必須有一個部隊(Receiver)來執行細節。
這裡我們讓總指揮官的命令包含：

    Breakthrough：突破
    Defense: 防禦
    Support: 支援

"""
class UtCommand(unittest.TestCase):

    def test_command(self):
        # 準備海陸空軍
        navy = ReceiverNavy()
        army = ReceiverArmy()
        airForce = ReceiverAirForce()
            
        """D-Day前:指揮官建立作戰計畫"""
                
        # 登陸作戰命令
        invokerLanding = Invoker()
        commands4Landing = [
                CmdBreakthrough(navy),  # 海軍突破
                CmdDefense(army),    # 陸軍防守
                CmdSupport(airForce)     # 空軍支援
        ]
        
        for cmd in commands4Landing:
            invokerLanding.addCommand(cmd)

        # 登陸後作戰命令
        invokerLanded = Invoker()
        commandsLanded = [
            CmdBreakthrough(army),  # 陸軍突破
            CmdSupport(navy),   # 海軍支援
            CmdDefense(airForce)    # 空軍防守
        ]
        for cmd in commandsLanded:
            invokerLanded.addCommand(cmd)


        """D-Day:開始執行作戰計畫"""

        print("搶灘作戰開始!-----------------")
        invokerLanding.invoke()

        isEnemyTough = True
        if(isEnemyTough):   # 敵方砲火猛烈=>更新命令
            # 取消空軍支援
            invokerLanded.cancelCommand(commandsLanded[2])
            # 改加入空軍突破
            invokerLanded.addCommand(CmdBreakthrough(airForce))

        print("陸地作戰開始!-----------------")           
        invokerLanded.invoke()

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()