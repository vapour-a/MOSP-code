import jpype
import jpype.imports

# Auto-generated wrapper for jc
class jcWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = jc(*args, **kwargs)

    def a(self, $$0):
        return jc.a($$0)

    def b(self, $$0):
        return jc.b($$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def acq(self, $$0):
        return self.obj.acq($$0)
