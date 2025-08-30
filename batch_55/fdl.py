import jpype
import jpype.imports

# Auto-generated wrapper for fdl
class fdlWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fdl(*args, **kwargs)

    def fdl(self, $$0):
        return self.obj.fdl($$0)

    def a(self, $$0):
        return fdl.a($$0)

    def fem(self, ):
        return self.obj.fem()

    def a(self, ):
        return self.obj.a()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
