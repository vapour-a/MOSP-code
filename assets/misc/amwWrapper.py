import jpype
import jpype.imports

# Auto-generated wrapper for amw
class amwWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = amw(*args, **kwargs)

    def a(self, $$0):
        return amw.a($$0)

    def acq(self, $$0):
        return self.obj.acq($$0)
