"""
The client code picks a concrete strategy and passes it to the context.
The client should be aware of the differences between strategies in order to make the right choice.
"""
from behavioral.strategy.concrete_strategies import ConcreteStrategyA, ConcreteStrategyB
from behavioral.strategy.context import Context

context = Context(ConcreteStrategyA())
print("Client: Strategy is set to normal sorting.")
context.do_some_business_logic()
print()

print("Client: Strategy is set to reverse sorting.")
context.strategy = ConcreteStrategyB()
context.do_some_business_logic()
