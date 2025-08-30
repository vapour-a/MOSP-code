import jpype
import jpype.imports

# Auto-generated wrapper for fvw
class fvwWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fvw(*args, **kwargs)

    def fvw(self, $$0, $$1, $$2):
        return self.obj.fvw($$0, $$1, $$2)

    def fuu(self, $$1):
        return self.obj.fuu($$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$1, $$0):
        return self.obj.a($$1, $$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def close(self, ):
        return self.obj.close()
