"""
Intent

Memento is a behavioral design pattern that lets you save and restore the previous state of an object without revealing the details of its implementation.

Problem

Imagine that you’re creating a text editor app. In addition to simple text editing, your editor can format text, insert inline images, etc.

At some point, you decided to let users undo any operations carried out on the text. This feature has become so common over the years that 
nowadays people expect every app to have it. For the implementation, you chose to take the direct approach. Before performing any operation, 
the app records the state of all objects and saves it in some storage. Later, when a user decides to revert an action, 
the app fetches the latest snapshot from the history and uses it to restore the state of all objects.

Let’s think about those state snapshots. How exactly would you produce one? You’d probably need to go over all the fields in an object and copy their values into storage. However, this would only work if the object had quite relaxed access restrictions to its contents. Unfortunately, most real objects won’t let others peek inside them that easily, hiding all significant data in private fields.

Ignore that problem for now and let’s assume that our objects behave like hippies: preferring open relations and keeping their state public. 
While this approach would solve the immediate problem and let you produce snapshots of objects’ states at will, it still has some serious issues. 
In the future, you might decide to refactor some of the editor classes, or add or remove some of the fields. Sounds easy, 
but this would also require chaining the classes responsible for copying the state of the affected objects.

But there’s more. Let’s consider the actual “snapshots” of the editor’s state. What data does it contain? At a bare minimum, it must contain the actual text, 
cursor coordinates, current scroll position, etc. To make a snapshot, you’d need to collect these values and put them into some kind of container.

Most likely, you’re going to store lots of these container objects inside some list that would represent the history. 
Therefore the containers would probably end up being objects of one class. The class would have almost no methods, 
but lots of fields that mirror the editor’s state. To allow other objects to write and read data to and from a snapshot, 
you’d probably need to make its fields public. That would expose all the editor’s states, private or not. 
Other classes would become dependent on every little change to the snapshot class, which would otherwise happen within private fields and 
methods without affecting outer classes.

It looks like we’ve reached a dead end: you either expose all internal details of classes, making them too fragile, 
or restrict access to their state, making it impossible to produce snapshots. Is there any other way to implement the "undo"?
"""

"""
Usage examples: The Memento’s principle can be achieved using the serialization, which is quite common in Python. 
While it’s not the only and the most efficient way to make snapshots of an object’s state, 
it still allows storing state backups while protecting the originator’s structure from other objects.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits


class Originator():
    """
    The Originator holds some important state that may change over time. It also
    defines a method for saving the state inside a memento and another method
    for restoring the state from it.
    """

    _state = None
    """
    For the sake of simplicity, the originator's state is stored inside a single
    variable.
    """

    def __init__(self, state):
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_something(self):
        """
        The Originator's business logic may affect its internal state.
        Therefore, the client should backup the state before launching methods
        of the business logic via the save() method.
        """

        print("Originator: I'm doing something important.")
        self._state = self._generate_random_string(30)
        print(f"Originator: and my state has changed to: {self._state}")

    def _generate_random_string(self, length=10):
        return "".join(sample(ascii_letters, length))

    def save(self):
        """
        Saves the current state inside a memento.
        """

        return ConcreteMemento(self._state)

    def restore(self, memento):
        """
        Restores the Originator's state from a memento object.
        """

        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Memento(ABC):
    """
    The Memento interface provides a way to retrieve the memento's metadata,
    such as creation date or name. However, it doesn't expose the Originator's
    state.
    """

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_date(self):
        pass


class ConcreteMemento(Memento):
    def __init__(self, state):
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self):
        """
        The Originator uses this method when restoring its state.
        """
        return self._state

    def get_name(self):
        """
        The rest of the methods are used by the Caretaker to display metadata.
        """

        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self):
        return self._date


class Caretaker():
    """
    The Caretaker doesn't depend on the Concrete Memento class. Therefore, it
    doesn't have access to the originator's state, stored inside the memento. It
    works with all mementos via the base Memento interface.
    """

    def __init__(self, originator):
        self._mementos = []
        self._originator = originator

    def backup(self):
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self):
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\nClient: Once more!\n")
    caretaker.undo()