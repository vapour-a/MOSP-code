import jpype
import jpype.imports

# Auto-generated wrapper for edo
class edoWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = edo(*args, **kwargs)

    def a(self, $$0, $$1):
        return edo.a($$0, $$1)

    def acq(self, $$0):
        return self.obj.acq($$0)

    def edm(self, $$1):
        return self.obj.edm($$1)

    def a(self, ):
        return edo.a()
