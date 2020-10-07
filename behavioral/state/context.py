from abc import ABC
from typing import Optional


class State(object):
    pass


class Context(ABC):
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    # A reference to the current state of the Context.
    _state: Optional[State] = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State) -> None:
        """
        The Context allows changing the State object at runtime.
        """

        print(f"Context: Transition to {type(state).__name__ }")
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()
