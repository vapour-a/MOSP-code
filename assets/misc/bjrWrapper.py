import jpype
import jpype.imports

# Auto-generated wrapper for bjr
class bjrWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bjr(*args, **kwargs)

    def a(self, $$0, $$1):
        return bjr.a($$0, $$1)

    def MutableInt(self, 0):
        return self.obj.MutableInt(0)
