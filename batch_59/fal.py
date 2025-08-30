import jpype
import jpype.imports

# Auto-generated wrapper for fal
class falWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fal(*args, **kwargs)

    def fal(self, $$0):
        return self.obj.fal($$0)

    def c(self, ):
        return fal.c()

    def fem(self, ):
        return self.obj.fem()

    def fei(self, 0.001F):
        return self.obj.fei(0.001F)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()
