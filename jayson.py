from typing import Any
import json
from sugar import *
# Load memory
class Jayson:
    def __init__(self):
        try:
            with open('memory.json', 'r') as f:
                self.memory = json.load(f)
        except FileNotFoundError:
            self.memory = {}
    
    def save(self):
        with open('memory.json', 'w') as f:
            json.dump(self.memory, f)
    
    def __call__(self, d : dict[str,Any] = {},/, **c: Any):
        d.update(c)
        self.memory.update(d)
        self.save()

    def __getitem__(self, index : str):
        return self.memory[index] if index in self.memory.keys() else ""