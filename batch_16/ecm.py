import jpype
import jpype.imports

# Auto-generated wrapper for ecm
class ecmWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ecm(*args, **kwargs)

    def a(self, $$0, $$1):
        return ecm.a($$0, $$1)

    def acq(self, $$0):
        return self.obj.acq($$0)

    def ecl(self, $$1):
        return self.obj.ecl($$1)

    def a(self, ):
        return ecm.a()

    def a(self, $$0):
        return self.obj.a($$0)

    def b(self, $$0):
        return self.obj.b($$0)
