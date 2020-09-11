"""
Concrete Products provide various implementations of the Product interface.
"""

from IProduct import IProduct


class ConcreteProduct1(IProduct):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(IProduct):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"
