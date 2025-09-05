import jpype
import jpype.imports

# Auto-generated wrapper for brn
class brnWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = brn(*args, **kwargs)

    def r(self, ):
        return self.obj.r()

    def w(self, paramBoolean):
        return self.obj.w(paramBoolean)

    def l(self, paramcfz):
        return self.obj.l(paramcfz)

    def c(self, paramqr):
        return self.obj.c(paramqr)

    def b(self, ):
        return self.obj.b()

    def w(self, ):
        return self.obj.w()

    def a(self, $$0, $$1):
        return brn.a($$0, $$1)

    def a(self, $$0, $$1):
        return brn.a($$0, $$1)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)
