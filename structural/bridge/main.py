"""
The client code should be able to work with any pre-configured abstraction-
implementation combination.
"""
from abstractions import Abstraction
from IImplementation import Implementation
from implementations import ConcreteImplementationA, ConcreteImplementationB


def client_code(abstraction: Abstraction) -> None:
    """
    Except for the initialization phase, where an Abstraction object gets
    linked with a specific Implementation object, the client code should only
    depend on the Abstraction class. This way the client code can support any
    abstraction-implementation combination.
    """

    print(abstraction.operation(), end="")


implementation = ConcreteImplementationA()
abstraction = Abstraction(implementation)

client_code(abstraction)


print("\n")

implementation = ConcreteImplementationB()
abstraction = Abstraction(implementation)

client_code(abstraction)
