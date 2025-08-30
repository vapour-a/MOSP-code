import jpype
import jpype.imports

# Auto-generated wrapper for fbu
class fbuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fbu(*args, **kwargs)

    def fbu(self, $$0):
        return self.obj.fbu($$0)

    def b(self, ):
        return fbu.b()

    def fem(self, ):
        return self.obj.fem()

    def fei(self, 0.5F):
        return self.obj.fei(0.5F)

    def a(self, ):
        return self.obj.a()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def c(self, ):
        return self.obj.c()
