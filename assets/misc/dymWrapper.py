import jpype
import jpype.imports

# Auto-generated wrapper for dym
class dymWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dym(*args, **kwargs)

    def dym(self, $$0, $$1, $$2):
        return self.obj.dym($$0, $$1, $$2)

    def a(self, $$0):
        return dym.a($$0)

    def dym(self, $$1, $$2, $$3):
        return self.obj.dym($$1, $$2, $$3)

    def a(self, ):
        return self.obj.a()

    def qr(self, ):
        return self.obj.qr()

    def b(self, ):
        return self.obj.b()

    def c(self, ):
        return self.obj.c()

    def d(self, ):
        return self.obj.d()

    def e(self, ):
        return self.obj.e()

    def a(self, this.a):
        return self.obj.a(this.a)

    def a(self, $$0):
        return dym.a($$0)
