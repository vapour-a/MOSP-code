import jpype
import jpype.imports

# Auto-generated wrapper for ane
class aneWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ane(*args, **kwargs)

    def a(self, $$0):
        return ane.a($$0)

    def acq(self, $$0):
        return self.obj.acq($$0)
