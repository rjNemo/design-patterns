"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""
from behavioral.observer.observer import Observer
from behavioral.observer.subject import Subject


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject.state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject.state == 0 or subject.state >= 2:
            print("ConcreteObserverB: Reacted to the event")
