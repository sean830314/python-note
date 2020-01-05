#!/usr/bin/python
# -*- coding: UTF-8 -*-
from BaseLogger import TextLogger,BaseLogger
from MyTask import MyTask

def main():
    logger = TextLogger() # Current release
    #logger = DbLogger() # Refine in next release
    task = MyTask(logger)
    task.run()
"""
策略模式

    定義一系列的演算法，並且把這些算法，
    用介面封裝到有公共介面的策略類中，使他們可以互相替換。

    策略模式用策略的介面來替換在某個實體ˋ中的方法，
    可以經由替換不同的策略使得物件擁有不同的行為。
    經過策略的組合，我們得以獲得行為不同的物件。

優點：

* 靈活的替換不同的行為（演算法）
* 策略拓展容易
* 避免使用很多if else

缺點：

* 必須自行決定要使用哪種策略
* 可能產生很多策略類
"""
if __name__ == '__main__':
    main()