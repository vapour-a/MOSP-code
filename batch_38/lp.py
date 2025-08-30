import jpype
import jpype.imports

# Auto-generated wrapper for lp
class lpWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = lp(*args, **kwargs)

    def acq(self, "recipes/root"):
        return self.obj.acq("recipes/root")

    def a(self, paramString, paramam):
        return self.obj.a(paramString, paramam)

    def a(self, paramString):
        return self.obj.a(paramString)

    def a(self, ):
        return self.obj.a()

    def a(self, paramConsumer, paramacq):
        return self.obj.a(paramConsumer, paramacq)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def acq(self, $$1):
        return self.obj.acq($$1)

    def IllegalStateException(self, one"):
        return self.obj.IllegalStateException(one")

    def a(self, $$0):
        return lp.a($$0)
