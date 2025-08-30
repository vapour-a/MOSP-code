import jpype
import jpype.imports

# Auto-generated wrapper for bdf
class bdfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bdf(*args, **kwargs)

    def a(self, paramapf):
        return self.obj.a(paramapf)
