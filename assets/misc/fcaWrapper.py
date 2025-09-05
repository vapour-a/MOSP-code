import jpype
import jpype.imports

# Auto-generated wrapper for fca
class fcaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fca(*args, **kwargs)

    def fca(self, $$0):
        return self.obj.fca($$0)

    def b(self, ):
        return fca.b()

    def fem(self, ):
        return self.obj.fem()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, ):
        return self.obj.a()
