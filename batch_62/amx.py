import jpype
import jpype.imports

# Auto-generated wrapper for amx
class amxWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = amx(*args, **kwargs)

    def a(self, $$0):
        return amx.a($$0)

    def acq(self, $$0):
        return self.obj.acq($$0)
