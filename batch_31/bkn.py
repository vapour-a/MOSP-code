import jpype
import jpype.imports

# Auto-generated wrapper for bkn
class bknWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bkn(*args, **kwargs)

    def a(self, $$0, $$1):
        return bkn.a($$0, $$1)

    def MutableLong(self, 0L):
        return self.obj.MutableLong(0L)
