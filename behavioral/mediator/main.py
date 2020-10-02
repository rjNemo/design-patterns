"""The client code."""
from behavioral.mediator.components import Component1, Component2
from behavioral.mediator.concrete_mediator import ConcreteMediator

c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)

print("Client triggers operation A.")
c1.do_a()

print("")
print("Client triggers operation D.")
c2.do_d()
