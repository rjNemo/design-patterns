from dataclasses import dataclass

from IImplementation import Implementation


@dataclass
class Abstraction:
    """
    The Abstraction defines the interface for the "control" part of the two
    class hierarchies. It maintains a reference to an object of the
    Implementation hierarchy and delegates all of the real work to this object.
    """

    implementation: Implementation

    def operation(self) -> str:
        return f"Abstraction: Base operation with:\n{self.implementation.operation_implementation()}"


class ExtendedAbstraction(Abstraction):
    """
    You can extend the Abstraction without changing the Implementation classes.
    """

    def operation(self) -> str:
        return f"""ExtendedAbstraction: Extended operation with:\n
        {self.implementation.operation_implementation()}"""
