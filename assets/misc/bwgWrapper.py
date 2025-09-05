import jpype
import jpype.imports

# Auto-generated wrapper for bwg
class bwgWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bwg(*args, **kwargs)

    def a(self, parambfz, paramFloat):
        return self.obj.a(parambfz, paramFloat)
