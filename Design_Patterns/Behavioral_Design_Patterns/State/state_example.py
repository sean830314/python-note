"""
Intent

State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. 
It appears as if the object changed its class.

Problem

The State pattern is closely related to the concept of a Finite-State Machine.

The main idea is that, at any given moment, there’s a finite number of states which a program can be in. Within any unique state, 
the program behaves differently, and the program can be switched from one state to another instantaneously. However, depending on a current state, 
the program may or may not switch to certain other states. These switching rules, called transitions, are also finite and predetermined.

You can also apply this approach to objects. Imagine that we have a Document class. A document can be in one of three states: Draft, 
Moderation and Published. The publish method of the document works a little bit differently in each state:

    In Draft, it moves the document to moderation.
    In Moderation, it makes the document public, but only if the current user is an administrator.
    In Published, it doesn’t do anything at all.

State machines are usually implemented with lots of conditional operators (if or switch) that select the appropriate behavior depending on 
the current state of the object. Usually, this “state” is just a set of values of the object’s fields. 
Even if you’ve never heard about finite-state machines before, you’ve probably implemented a state at least once. 
Does the following code structure ring a bell

Real-World Analogy

The buttons and switches in your smartphone behave differently depending on the current state of the device:

    When the phone is unlocked, pressing buttons leads to executing various functions.
    When the phone is locked, pressing any button leads to the unlock screen.
    When the phone’s charge is low, pressing any button shows the charging screen.

"""

from abc import ABC, abstractmethod


class Context(ABC):
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    """
    A reference to the current state of the Context.
    """

    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, state):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def handle1(self):
        pass

    @abstractmethod
    def handle2(self):
        pass


"""
Concrete States implement various behaviors, associated with a state of the
Context.
"""


class ConcreteStateA(State):
    def handle1(self):
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self):
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle1(self):
        print("ConcreteStateB handles request1.")

    def handle2(self):
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())


if __name__ == "__main__":
    # The client code.

    context = Context(ConcreteStateA())
    context.request1()
    context.request2()
