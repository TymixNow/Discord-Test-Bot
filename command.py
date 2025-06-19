from collections.abc import Callable
from message_builder import MessageForm

noop = lambda *args: None
same = lambda x : x

class Commander:
    def __init__(self):
        pass
    def __call__(self, command : str, message : MessageForm):
        pass
class LeafCommander(Commander):
    def __init__(self, d : dict[str,tuple[Callable, Callable, bool] | Callable] = {},/, *, default : Callable = (lambda word: "") , **c: tuple[Callable, Callable, bool]):
        d.update(c)
        self.commands = d
        self.default = default
    def __call__(self, command: str, message : MessageForm):
        for key in self.commands.keys():
            if command.startswith(key):
                value_base : Callable | tuple = self.commands[key]
                value : tuple = value_base if not callable(value_base) else tuple([value_base, noop, False])
                message.rewrite(value[0].__call__(command.removeprefix(key)))
                if value[2]: message.redirect(value[1].__call__(command.removeprefix(key)))
                return 
        message.rewrite(self.default.__call__(command))
        return
class StemCommander(Commander):
    def __init__(self,d : dict[str, tuple[Commander,Callable, Callable, bool] | Commander] = {}, **c: tuple[Commander, Callable, Callable, bool] | Commander):
        self.commands = c
        self.commands.update(d)
    def __call__(self, command: str, message : MessageForm):
        for key in self.commands.keys():
            if command.startswith(key):
                value_base = self.commands[key]
                value : tuple = value_base if not callable(value_base) else tuple([value_base, same, noop, False])
                message.rewrite(value[1].__call__(value[0](command.removeprefix(key), message)))
                if value[3]: message.redirect(value[2].__call__(command.removeprefix(key)))
                return 