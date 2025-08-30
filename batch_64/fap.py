import jpype
import jpype.imports

# Auto-generated wrapper for fap
class fapWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fap(*args, **kwargs)

    def fap(self, $$0):
        return self.obj.fap($$0)

    def b(self, ):
        return fap.b()

    def fem(self, ):
        return self.obj.fem()

    def fei(self, 0.1F):
        return self.obj.fei(0.1F)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7)

    def a(self, ):
        return self.obj.a()
