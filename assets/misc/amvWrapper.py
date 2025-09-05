import jpype
import jpype.imports

# Auto-generated wrapper for amv
class amvWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = amv(*args, **kwargs)

    def a(self, $$0):
        return amv.a($$0)

    def acq(self, $$0):
        return self.obj.acq($$0)
