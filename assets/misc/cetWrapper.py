import jpype
import jpype.imports

# Auto-generated wrapper for cet
class cetWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cet(*args, **kwargs)

    def cet(self, $$0):
        return self.obj.cet($$0)

    def d(self, $$0):
        return cet.d($$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def a(self, this, $$0, $$1, $$2):
        return self.obj.a(this, $$0, $$1, $$2)

    def ak_(self, ):
        return self.obj.ak_()

    def g(self, ):
        return self.obj.g()
