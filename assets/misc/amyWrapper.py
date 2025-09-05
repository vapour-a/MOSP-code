import jpype
import jpype.imports

# Auto-generated wrapper for amy
class amyWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = amy(*args, **kwargs)

    def a(self, $$0):
        return amy.a($$0)

    def acq(self, $$0):
        return self.obj.acq($$0)
