import jpype
import jpype.imports

# Auto-generated wrapper for fsr
class fsrWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fsr(*args, **kwargs)

    def fsr(self, fqt<T, $$0):
        return self.obj.fsr(fqt<T, $$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9)

    def a(self, paramFloat):
        return self.obj.a(paramFloat)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()
