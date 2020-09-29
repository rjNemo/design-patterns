from creational.factory_method.ICreator import ICreator
from creational.factory_method.creators import ConcreteCreator1, \
    ConcreteCreator2


def client_code(creator: ICreator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit
    through its base interface. As long as the client keeps working with the
    creator via the base interface, you can pass it any creator's subclass.
    """

    print(
        f"Client: I'm not aware of the creator's class, but it still works.\n"
        f"{creator.some_operation()}",
        end="",
    )


print("App: Launched with the ConcreteCreator1.")
client_code(ConcreteCreator1())
print("\n")

print("App: Launched with the ConcreteCreator2.")
client_code(ConcreteCreator2())
