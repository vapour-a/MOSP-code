import jpype
import jpype.imports

# Auto-generated wrapper for ana
class anaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ana(*args, **kwargs)

    def a(self, $$0):
        return ana.a($$0)

    def acq(self, $$0):
        return self.obj.acq($$0)
