"""
Concrete Strategies implement the algorithm while following the base Strategy interface. The interface makes them
interchangeable in the Context.
"""
from behavioral.strategy.strategy import Strategy


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: list) -> list:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: list) -> list:
        return reversed(sorted(data))
