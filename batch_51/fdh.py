import jpype
import jpype.imports

# Auto-generated wrapper for fdh
class fdhWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fdh(*args, **kwargs)

    def fdh(self, $$0):
        return self.obj.fdh($$0)

    def a(self, $$0):
        return fdh.a($$0)

    def b(self, ):
        return fdh.b()

    def fem(self, ):
        return self.obj.fem()

    def fei(self, 0.02F):
        return self.obj.fei(0.02F)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, ):
        return self.obj.a()
