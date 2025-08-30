import jpype
import jpype.imports

# Auto-generated wrapper for fdv
class fdvWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fdv(*args, **kwargs)

    def fdv(self, $$0):
        return self.obj.fdv($$0)

    def c(self, ):
        return fdv.c()

    def fem(self, ):
        return self.obj.fem()

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
