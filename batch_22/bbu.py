import jpype
import jpype.imports

# Auto-generated wrapper for bbu
class bbuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bbu(*args, **kwargs)

    def a(self, paramSupplier):
        return self.obj.a(paramSupplier)
