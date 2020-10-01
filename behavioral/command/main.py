"""
The client code can parameterize an invoker with any commands.
"""
from behavioral.command.commands import SimpleCommand, ComplexCommand
from behavioral.command.invoker import Invoker
from behavioral.command.receiver import Receiver

if __name__ == '__main__':
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say hi"))

    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Send email", "Save report"))

    invoker.do_something_important()
