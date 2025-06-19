def none(self, fix):
    return self if self is not None else fix
def str_none(self, fix, empty):
    return none(self,fix) if none(self,fix) != "" else empty