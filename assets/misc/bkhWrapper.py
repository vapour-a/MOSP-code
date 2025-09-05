import jpype
import jpype.imports

# Auto-generated wrapper for bkh
class bkhWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bkh(*args, **kwargs)

    def a(self, $$0, $$1, $$2):
        return bkh.a($$0, $$1, $$2)

    def MutableLong(self, 0L):
        return self.obj.MutableLong(0L)
