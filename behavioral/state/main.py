# The client code.
from behavioral.state.concrete_states import ConcreteStateA
from behavioral.state.context import Context

context = Context(ConcreteStateA())
context.request1()
context.request2()
