import jpype
import jpype.imports

# Auto-generated wrapper for fdd
class fddWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fdd(*args, **kwargs)

    def fdd(self, $$0):
        return self.obj.fdd($$0)

    def b(self, ):
        return fdd.b()

    def fem(self, ):
        return self.obj.fem()

    def c(self, ):
        return fdd.c()

    def fem(self, ):
        return self.obj.fem()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, ):
        return self.obj.a()
