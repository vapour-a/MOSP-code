import jpype
import jpype.imports

# Auto-generated wrapper for amu
class amuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = amu(*args, **kwargs)

    def a(self, $$0):
        return amu.a($$0)

    def acq(self, $$0):
        return self.obj.acq($$0)
