import jpype
import jpype.imports

# Auto-generated wrapper for drt
class drtWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = drt(*args, **kwargs)

    def a(self, $$0):
        return drt.a($$0)

    def acq(self, $$0):
        return self.obj.acq($$0)
