import jpype
import jpype.imports

# Auto-generated wrapper for fau
class fauWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fau(*args, **kwargs)

    def fau(self, $$0):
        return self.obj.fau($$0)

    def c(self, ):
        return fau.c()

    def fem(self, ):
        return self.obj.fem()

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
