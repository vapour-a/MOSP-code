import jpype
import jpype.imports

# Auto-generated wrapper for aqe
class aqeWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = aqe(*args, **kwargs)

    def aqe(self, $$0, $$1):
        return self.obj.aqe($$0, $$1)

    def aqe(self, $$0, $$1, $$2):
        return self.obj.aqe($$0, $$1, $$2)

    def IllegalArgumentException(self, storage, $$3):
        return self.obj.IllegalArgumentException(storage, $$3)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()
