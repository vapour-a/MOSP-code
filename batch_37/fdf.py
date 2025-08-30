import jpype
import jpype.imports

# Auto-generated wrapper for fdf
class fdfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fdf(*args, **kwargs)

    def fdf(self, $$0):
        return self.obj.fdf($$0)

    def b(self, ):
        return fdf.b()

    def fem(self, ):
        return self.obj.fem()

    def fei(self, -0.5F):
        return self.obj.fei(-0.5F)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, ):
        return self.obj.a()

    def c(self, ):
        return self.obj.c()
