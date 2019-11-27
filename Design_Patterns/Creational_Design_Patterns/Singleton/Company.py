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
    company1 = Company.getCompany('google', '07777777777')
    company1.get_information()
    company2 = Company.getCompany('amazon', '09888888888')
    company2.get_information()
    print(company1 is company2)