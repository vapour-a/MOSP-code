import jpype
import jpype.imports

# Auto-generated wrapper for fdj
class fdjWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fdj(*args, **kwargs)

    def fdj(self, $$0):
        return self.obj.fdj($$0)

    def c(self, ):
        return fdj.c()

    def fem(self, ):
        return self.obj.fem()

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
