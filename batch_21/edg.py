import jpype
import jpype.imports

# Auto-generated wrapper for edg
class edgWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = edg(*args, **kwargs)

    def a(self, $$0, $$1):
        return edg.a($$0, $$1)

    def acq(self, $$0):
        return self.obj.acq($$0)

    def ede(self, $$1):
        return self.obj.ede($$1)

    def a(self, ):
        return edg.a()
