import jpype
import jpype.imports

# Auto-generated wrapper for dfc
class dfcWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dfc(*args, **kwargs)

    def BitSet(self, ):
        return self.obj.BitSet()

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def b(self, $$0, $$1):
        return self.obj.b($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, ):
        return self.obj.a()
