class Replacer:
    def __init__(self, d : dict[str,str] = {}, spacewise : bool = False, /, **c: str):
        d.update(c)
        self.replacements = d
        self.spacewise = spacewise
    def __call__(self, string : str) -> str:
        if self.spacewise:
            string = " ".join([(self.replacements[x] if x in self.replacements.keys() else x) for x in string.split()])
        else:
            for orig in self.replacements.keys():
                string = string.replace(orig.lower(), self.replacements[orig])
        return string