"""The client code"""

from behavioral.observer.concrete_observers import ConcreteObserverA, ConcreteObserverB


from behavioral.observer.concrete_subject import ConcreteSubject

subject = ConcreteSubject()


observer_a = ConcreteObserverA()
subject.attach(observer_a)

observer_b = ConcreteObserverB()
subject.attach(observer_b)


subject.some_business_logic()
subject.some_business_logic()

subject.detach(observer_a)

subject.some_business_logic()
