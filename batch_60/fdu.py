import jpype
import jpype.imports

# Auto-generated wrapper for fdu
class fduWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fdu(*args, **kwargs)

    def fdu(self, $$0):
        return self.obj.fdu($$0)

    def a(self, $$0):
        return fdu.a($$0)

    def fem(self, ):
        return self.obj.fem()

    def a(self, ):
        return self.obj.a()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)
