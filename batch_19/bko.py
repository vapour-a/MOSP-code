import jpype
import jpype.imports

# Auto-generated wrapper for bko
class bkoWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bko(*args, **kwargs)

    def a(self, $$0, $$1):
        return bko.a($$0, $$1)

    def MutableLong(self, 0L):
        return self.obj.MutableLong(0L)
