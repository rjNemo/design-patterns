from abc import ABC, abstractmethod

from AbstractProductA import AbstractProductA
from AbstractProductB import AbstractProductB


class AbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are
    usually able to collaborate among themselves. A family of products may have
    several variants, but the products of one variant are incompatible with
    products of another.
    """

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass
