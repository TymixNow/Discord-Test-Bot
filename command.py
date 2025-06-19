from collections.abc import Callable
from message_builder import MessageForm
noop = lambda *args: None
same = lambda x : x

class Commander:
    def __init__(self, **c):
        self.commands = c
        pass
    def __call__(self, command : str, message : MessageForm):
        return command
class LeafCommander(Commander):
    def __init__(self, action : tuple[Callable, Callable] | Callable = same):
        self.action = action
    def __call__(self, command: str, message : MessageForm):
        if isinstance(self.action, tuple):
            message.rewrite(self.action[0](message, command))
            message.redirect(self.action[1](message, command))
        else:
            message.rewrite(self.action(message, command))
        return message.text
class StemCommander(Commander):
    def __init__(self,d : dict[str, tuple[Commander,Callable, Callable, bool] | Commander] = {}, / , * , default : Commander = LeafCommander(lambda word, x:""), **c: tuple[Commander, Callable, Callable, bool] | Commander):
        super().__init__(**d,**c)
        self.default = default
    def __call__(self, command: str, message : MessageForm):
        has = False
        for key in self.commands.keys():
            if command.startswith(key):
                has = True
                value_base = self.commands[key]
                value : tuple = value_base if not isinstance(value_base, Commander) else tuple([value_base, same, noop, False])
                output = value[1].__call__(value[0](command.removeprefix(key), message))
                message.rewrite(output)
                if value[3]: message.redirect(value[2].__call__(command.removeprefix(key)))
        if not has:
            message.rewrite(self.default(command, message))
        return message.text