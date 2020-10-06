from structural.decorator.component import Component
from structural.decorator.concrete_component import ConcreteComponent
from structural.decorator.concrete_decorators import (
    ConcreteDecoratorA,
    ConcreteDecoratorB,
)


def client_code(component: Component):
    """
    The client code works with all objects using the Component interface. This
    way it can stay independent of the concrete classes of components it works
    with.
    """

    print(f"RESULT: {component.operation()}", end="")


if __name__ == "__main__":
    # This way the client code can support both simple components...
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as decorated ones.

    # Note how decorators can wrap not only simple components but the other
    # decorators as well.
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    client_code(decorator2)
