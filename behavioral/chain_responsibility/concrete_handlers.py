"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""
from typing import Optional, Any

from behavioral.chain_responsibility.abstract_handler import AbstractHandler


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == 'Banana':
            return f"Monkey: I'll eat the {request}"
        return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == 'Nut':
            return f"Squirrel: I'll eat the {request}"
        return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == 'MeatBall':
            return f"Dog: I'll eat the {request}"
        return super().handle(request)
