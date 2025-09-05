import jpype
import jpype.imports

# Auto-generated wrapper for cti
class ctiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cti(*args, **kwargs)

    def cti(self, $$0):
        return self.obj.cti($$0)

    def a(self, ):
        return cti.a()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def b(self, $$0, $$1, $$2, $$3):
        return self.obj.b($$0, $$1, $$2, $$3)

    def d(self, $$0, $$1, $$2):
        return self.obj.d($$0, $$1, $$2)
