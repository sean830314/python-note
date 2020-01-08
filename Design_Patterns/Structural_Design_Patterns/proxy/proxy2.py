"""
Intent

Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

Real-World Analogy

A credit card is a proxy for a bank account, which is a proxy for a bundle of cash. Both implement the same interface: they can be used for making a payment. A consumer feels great because there’s no need to carry loads of cash around. A shop owner is also happy since the income from a transaction gets added electronically to the shop’s bank account without the risk of losing the deposit or getting robbed on the way to the bank.
"""
class Image():
    def display():
        pass

class RealImage(Image):

    def __init__(self, file_name):
        self.file_name = file_name
        self.load_from_disk()

    def display(self):
        print("Displaying {}".format(self.file_name))

    def load_from_disk(self):
        print("Loading {}".format(self.file_name))

class ProxyImage(Image):

    def __init__(self, file_name):
        self.file_name = file_name
        self.proxy_object = None

    def display(self):
        if self.proxy_object is None:
            self.proxy_object = RealImage(self.file_name)
        self.proxy_object.display()

def main():
    image = ProxyImage("test.jpg")
    image.display()
    print("")
    image.display()

if __name__=='__main__':
    main()
