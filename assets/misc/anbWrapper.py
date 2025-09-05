import jpype
import jpype.imports

# Auto-generated wrapper for anb
class anbWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = anb(*args, **kwargs)

    def a(self, $$0):
        return anb.a($$0)

    def acq(self, $$0):
        return self.obj.acq($$0)
