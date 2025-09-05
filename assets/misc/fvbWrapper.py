import jpype
import jpype.imports

# Auto-generated wrapper for fvb
class fvbWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fvb(*args, **kwargs)

    f = fvb.f
    g = fvb.g
    h = fvb.h
    def a(self, $$0, $$1):
        return fvb.a($$0, $$1)

    def fva(self, $$1):
        return self.obj.fva($$1)

    def acq(self, $$0):
        return self.obj.acq($$0)

    def IllegalStateException(self, $$3):
        return self.obj.IllegalStateException($$3)
