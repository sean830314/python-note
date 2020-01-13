from abc import ABC, abstractmethod
from Cor_models import Content, DataFactory
"""
Intent

Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers. 
Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

Problem

Imagine that you’re working on an online ordering system. 
You want to restrict access to the system so only authenticated users can create orders. Also, 
users who have administrative permissions must have full access to all orders.
After a bit of planning, you realized that these checks must be performed sequentially. 
The application can attempt to authenticate a user to the system whenever it receives a request that contains the user’s credentials. 
However, if those credentials aren’t correct and authentication fails, there’s no reason to proceed with any other checks.

During the next few months, you implemented several more of those sequential checks.

1. One of your colleagues suggested that it’s unsafe to pass raw data straight to the ordering system. 
    So you added an extra validation step to sanitize the data in a request.

2. Later, somebody noticed that the system is vulnerable to brute force password cracking. To negate this, 
    you promptly added a check that filters repeated failed requests coming from the same IP address.

3. Someone else suggested that you could speed up the system by returning cached results on repeated requests containing the same data. 
    Hence, you added another check which lets the request pass through to the system only if there’s no suitable cached response.

However, there’s a slightly different approach (and it’s a bit more canonical) in which, upon receiving a request, 
a handler decides whether it can process it. If it can, it doesn’t pass the request any further. 
So it’s either only one handler that processes the request or none at all. 
This approach is very common when dealing with events in stacks of elements within a graphical user interface.

For instance, when a user clicks a button, the event propagates through the chain of GUI elements that starts with the button, 
goes along its containers (like forms or panels), and ends up with the main application window. 
The event is processed by the first element in the chain that’s capable of handling it. 
This example is also noteworthy because it shows that a chain can always be extracted from an object tree.


Real-World Analogy

You’ve just bought and installed a new piece of hardware on your computer. Since you’re a geek, 
the computer has several operating systems installed. You try to boot all of them to see whether the hardware is supported. 
Windows detects and enables the hardware automatically. However, your beloved Linux refuses to work with the new hardware. 
With a small flicker of hope, you decide to call the tech-support phone number written on the box.

The first thing you hear is the robotic voice of the autoresponder. It suggests nine popular solutions to various problems, 
none of which are relevant to your case. After a while, the robot connects you to a live operator.

Alas, the operator isn’t able to suggest anything specific either. He keeps quoting lengthy excerpts from the manual, 
refusing to listen to your comments. After hearing the phrase “have you tried turning the computer off and on again?” 
for the 10th time, you demand to be connected to a proper engineer.

Eventually, the operator passes your call to one of the engineers, 
who had probably longed for a live human chat for hours as he sat in his lonely server room in the dark basement of some office building. 
The engineer tells you where to download proper drivers for your new hardware and how to install them on Linux. Finally, the solution! 
You end the call, bursting with joy.
"""
class HandlerBase(ABC):    

    @property
    @abstractmethod
    def next(self):
        pass

    @next.setter
    @abstractmethod
    def next(self, val):
        pass

    @abstractmethod
    def action(self, localization):
        pass
        

class Handler(HandlerBase):
    _next = None
    
    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, val):
        self._next = val

    def action(self, localization):
        if (self._next == None):
            self._next = ReceiverZh()

        return self._next.action(localization)


class ReceiverZh(HandlerBase):
    _next=None
    
    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, val):
        self._next = val        

    def action(self, localization):
        #Action
        if (localization=="zh-TW"):
            content =  Content(DataFactory.countryZh(),DataFactory.cityZh())
            print("{0} {1}".format(content.country, content.city))
            return content
        else:
            print("Not zh-TW, go to next receiver...")

        #Go to next
        if (self._next == None):
            self._next = ReceiverCn()

        return self._next.action(localization)



class ReceiverCn(HandlerBase):
    _next=None
    
    @property
    def next(self):
        return self._next

    @next.setter
    def value(self, val):
        self._next = val

    def action(self, localization):
        #Action
        if (localization=="zh-CN"):
            content =  Content(DataFactory.countryCn(), DataFactory.cityCn())
            print("{0} {1}".format(content.country, content.city))
            return content
        else:
            print("Not zh-CN, go to next receiver...")

        #Go to next
        if (self._next == None):
            self._next = ReceiverEn()

        return self._next.action(localization)


class ReceiverEn(HandlerBase):
    _next=None
    
    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, val):
        self._next = val

    def action(self, localization):
        #Action
        if (localization=="en-US"):
            content =  Content(DataFactory.countryEn(),DataFactory.cityEn())
            print("{0} {1}".format(content.country, content.city))               
            return content
        else:
            print("Not en-US, go to next receiver...")

        #Go to next
        if (self._next == None):
            self._next = ReceiverException()

        return self._next.action(localization)


class ReceiverException(HandlerBase):
    _next=None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, val):
        self._next = val

    def action(self, localization):
        #Action
        err = "Error! Create a receiver for " + localization +"!"
        print(err)
        raise ValueError(err)