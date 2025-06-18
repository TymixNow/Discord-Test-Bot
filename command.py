from collections.abc import Callable

class LeafCommander:
    def __init__(self, d : dict[str,Callable] = {},/, *, default : Callable = (lambda word: "") , **c: Callable):
        d.update(c)
        self.commands = d
        self.default = default
    def __call__(self, command: str):
        for key in self.commands.keys():
            if command.startswith(key):
                return self.commands[key].__call__(command.removeprefix(key))
        return self.default.__call__(command)
class StemCommander:
    def __init__(self, **c: tuple[Callable, Callable]):
        self.commands = c
    def __call__(self, command: str):
        for key in self.commands.keys():
            if command.startswith(key):
                return self.commands[key][1].__call__(self.commands[key][0].__call__(command.removeprefix(key)))