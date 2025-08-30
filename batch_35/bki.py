import jpype
import jpype.imports

# Auto-generated wrapper for bki
class bkiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bki(*args, **kwargs)

    def a(self, $$0, $$1, $$2, $$3):
        return bki.a($$0, $$1, $$2, $$3)

    def MutableLong(self, 0L):
        return self.obj.MutableLong(0L)
