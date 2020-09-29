"""
Each Concrete Implementation corresponds to a specific platform and implements
the Implementation interface using that platform's API.
"""
from structural.bridge.IImplementation import Implementation


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."
