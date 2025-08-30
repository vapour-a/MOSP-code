import jpype
import jpype.imports

# Auto-generated wrapper for fdn
class fdnWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fdn(*args, **kwargs)

    def fdn(self, $$0):
        return self.obj.fdn($$0)

    def c(self, ):
        return fdn.c()

    def fem(self, ):
        return self.obj.fem()

    def b(self, ):
        return self.obj.b()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7)
