class Replacer:
    def __init__(self, d : dict[str,str] = {},/, **c: str):
        d.update(c)
        self.replacements = d
    def __call__(self, string : str):
        for orig in self.replacements.keys():
            string = string.replace(orig.lower(), self.replacements[orig])
            string = string.replace(orig.upper(), self.replacements[orig])
        return string