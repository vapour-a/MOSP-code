import jpype
import jpype.imports

# Auto-generated wrapper for fcz
class fczWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fcz(*args, **kwargs)

    def fcz(self, $$0):
        return self.obj.fcz($$0)

    def a(self, $$0):
        return fcz.a($$0)

    def b(self, $$0):
        return fcz.b($$0)

    def b(self, ):
        return fcz.b()

    def fem(self, ):
        return self.obj.fem()

    def a(self, ):
        return self.obj.a()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
