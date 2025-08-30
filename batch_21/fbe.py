import jpype
import jpype.imports

# Auto-generated wrapper for fbe
class fbeWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fbe(*args, **kwargs)

    def fbe(self, $$0):
        return self.obj.fbe($$0)

    def a(self, $$0):
        return fbe.a($$0)

    def b(self, ):
        return fbe.b()

    def fem(self, ):
        return self.obj.fem()

    def a(self, ):
        return self.obj.a()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
