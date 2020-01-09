""""
Let’s say that you want to build a news website and you want to show different content for different users. You want to give paid users full access to articles, without any ads. At the same time, you want to give free users some excerpts from the articles, with some ads on the page. Finally, you want to show a call to action to all free users, so you can hopefully convert them to paid users.


Client 	        Interface 	        Implementation
the user 	the UI of the website 	what it's drawn in each UI component

The Interface is the UI of website. There are free users and paid users, so there are two interfaces to build: one with ads, excerpts and a call to action (free version) and another one with full articles (paid version).
"""
from abc import ABC, abstractmethod


# Abstract Interface (aka Handle) used by the client
class Website(ABC):

    def __init__(self, implementation):
        # encapsulate an instance of a concrete implementation class
        self._implementation = implementation

    def __str__(self):
        return 'Interface: {}; Implementation: {}'.format(
            self.__class__.__name__, self._implementation.__class__.__name__)

    @abstractmethod
    def show_page(self):
        pass

# Concrete Interface 1
class FreeWebsite(Website):

    def show_page(self):
        ads = self._implementation.get_ads()
        text = self._implementation.get_excerpt()
        call_to_action = self._implementation.get_call_to_action()
        print(ads)
        print(text)
        print(call_to_action)
        print('')

# Concrete Interface 2
class PaidWebsite(Website):

    def show_page(self):
        text = self._implementation.get_article()
        print(text)
        print('')

# Abstract Implementation (aka Body) decoupled from the client
class Implementation(ABC):

    def get_excerpt(self):
        return 'excerpt from the article'

    def get_article(self):
        return 'full article'

    def get_ads(self):
        return 'some ads'

    @abstractmethod
    def get_call_to_action(self):
        pass

# Concrete Implementation 1
class ImplementationA(Implementation):

    def get_call_to_action(self):
        return 'Pay 10 $ a month to remove ads'



# Concrete Implementation 2
class ImplementationB(Implementation):

    def get_call_to_action(self):
        return 'Remove ads with just 10 $ a month'

# Client
def main():
    a_free = FreeWebsite(ImplementationA())
    print(a_free)
    a_free.show_page()  # the client interacts only with the interface

    b_free = FreeWebsite(ImplementationB())
    print(b_free)
    b_free.show_page()

    a_paid = PaidWebsite(ImplementationA())
    print(a_paid)
    a_paid.show_page()

    b_paid = PaidWebsite(ImplementationB())
    print(b_paid)
    b_paid.show_page()

if __name__ == '__main__':
    main()
