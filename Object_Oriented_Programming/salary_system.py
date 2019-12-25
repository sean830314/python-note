"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):
    """Employee"""

    def __init__(self, name):
        """
        init method

        :param :name 
        """
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        """
        get month salary

        :return: month salary
        """
        pass


class Manager(Employee):
    """Manager"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """Programmer"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150.0 * self._working_hour


class Salesman(Employee):
    """Salesman"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05


def main():
    emps = [
        Manager('tom'), Programmer('jimmy'),
        Salesman('jack'), Salesman('frank'),
        Programmer('jason')
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input('Please enter %s working hours this month: ' % emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = float(input('Please enter %s sales for the month: ' % emp.name))
        # Polymorphism in Python
        print('%s salary this month: ￥%s' %
              (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()