import jpype
import jpype.imports

# Auto-generated wrapper for bkj
class bkjWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bkj(*args, **kwargs)

    def a(self, $$0, $$1, $$2, $$3, $$4):
        return bkj.a($$0, $$1, $$2, $$3, $$4)

    def MutableLong(self, 0L):
        return self.obj.MutableLong(0L)
