import jpype
import jpype.imports

# Auto-generated wrapper for bds
class bdsWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bds(*args, **kwargs)

    def a(self, parambdq):
        return self.obj.a(parambdq)
