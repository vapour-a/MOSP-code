import jpype
import jpype.imports

# Auto-generated wrapper for fdy
class fdyWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fdy(*args, **kwargs)

    def fdy(self, $$0):
        return self.obj.fdy($$0)

    def a(self, ):
        return fdy.a()

    def fem(self, ):
        return self.obj.fem()

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7)
