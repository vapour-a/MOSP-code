import jpype
import jpype.imports

# Auto-generated wrapper for amr
class amrWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = amr(*args, **kwargs)

    def a(self, $$0, $$1):
        return amr.a($$0, $$1)

    def acq(self, $$0):
        return self.obj.acq($$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def amq(self, $$1):
        return self.obj.amq($$1)
