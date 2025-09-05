import jpype
import jpype.imports

# Auto-generated wrapper for cnr
class cnrWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cnr(*args, **kwargs)

    def a(self, $$0):
        return cnr.a($$0)

    def acq(self, $$0):
        return self.obj.acq($$0)
