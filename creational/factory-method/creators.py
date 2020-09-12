"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""

from __future__ import annotations

from ICreator import ICreator
from products import ConcreteProduct1, ConcreteProduct2


class ConcreteCreator1(ICreator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def factory_method(self) -> ConcreteProduct1:
        return ConcreteProduct1()


class ConcreteCreator2(ICreator):

    def factory_method(self) -> ConcreteProduct2:
        return ConcreteProduct2()
