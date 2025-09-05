import jpype
import jpype.imports

# Auto-generated wrapper for fmu
class fmuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fmu(*args, **kwargs)

    def BitSet(self, a):
        return self.obj.BitSet(a)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def toString(self, ):
        return self.obj.toString()

    def StringBuilder(self, ):
        return self.obj.StringBuilder()
