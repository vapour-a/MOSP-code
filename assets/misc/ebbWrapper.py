import jpype
import jpype.imports

# Auto-generated wrapper for ebb
class ebbWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ebb(*args, **kwargs)

    def a(self, $$0, $$1):
        return ebb.a($$0, $$1)

    def acq(self, $$0):
        return self.obj.acq($$0)

    def eba(self, $$1):
        return self.obj.eba($$1)

    def a(self, ):
        return ebb.a()

    def a(self, BiFunction<cfz, dzk, $$0):
        return self.obj.a(BiFunction<cfz, dzk, $$0)
