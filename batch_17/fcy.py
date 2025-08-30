import jpype
import jpype.imports

# Auto-generated wrapper for fcy
class fcyWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fcy(*args, **kwargs)

    def fcy(self, $$0):
        return self.obj.fcy($$0)

    def a(self, ):
        return fcy.a()

    def fem(self, ):
        return self.obj.fem()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def d(self, ):
        return self.obj.d()

    def b(self, ):
        return self.obj.b()

    def c(self, ):
        return self.obj.c()
