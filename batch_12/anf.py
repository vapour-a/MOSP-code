import jpype
import jpype.imports

# Auto-generated wrapper for anf
class anfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = anf(*args, **kwargs)

    def a(self, $$0):
        return anf.a($$0)

    def acq(self, $$0):
        return self.obj.acq($$0)
