# design pattern singleton
class Company:
    __single = None

    def __init__(self, name, phone):
        self._name = name
        self._phone = phone

    def getCompany(name, phone):
        if not Company.__single:
            Company.__single = Company(name, phone)
        return Company.__single

    def get_information(self):
        print("Company name: {}, phone: {}".format(self._name, self._phone))


if __name__ == "__main__":
    """
    單例模式

        定義：只有一個實例，而且自行實例化並向整個系統提供這個實例。

        屬於創建模式，
        這個模式涉及到一個單一的類別，他必須要創建自己的實例，
        並且確保只有單一個對象被創建。
        這個類別提供一個方法訪問其被創建的唯一一個對象。

    Singleton：很簡單的只有一個類別，其中提供存取自己物件的方法，確保整個系統只有實例化一個物件。
    
    有幾種方式可以實現單例模式
    懶散(Lazy)模式（線程不安全）
    懶散模式（線程安全）
    積極模式
    雙重鎖 (Double ChockLock)
    登記式（靜態內部類）
    枚舉 (enumeration)


    """
    company1 = Company.getCompany('google', '07777777777')
    company1.get_information()
    company2 = Company.getCompany('amazon', '09888888888')
    company2.get_information()
    print(company1 is company2)