import jpype
import jpype.imports

# Auto-generated wrapper for fdx
class fdxWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fdx(*args, **kwargs)

    def fdx(self, $$0):
        return self.obj.fdx($$0)

    def c(self, ):
        return fdx.c()

    def fej(self, ):
        return self.obj.fej()

    def fei(self, 0.5F):
        return self.obj.fei(0.5F)

    def fei(self, 0.05F):
        return self.obj.fei(0.05F)

    def a(self, $$0):
        return fdx.a($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0):
        return self.obj.a($$0)
