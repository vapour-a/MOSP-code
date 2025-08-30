import jpype
import jpype.imports

# Auto-generated wrapper for fdm
class fdmWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fdm(*args, **kwargs)

    def fdm(self, $$0):
        return self.obj.fdm($$0)

    def a(self, $$0):
        return fdm.a($$0)

    def fem(self, ):
        return self.obj.fem()

    def a(self, ):
        return self.obj.a()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
