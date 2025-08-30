import jpype
import jpype.imports

# Auto-generated wrapper for foc
class focWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = foc(*args, **kwargs)

    def acq(self, "textures/entity/blaze.png"):
        return self.obj.acq("textures/entity/blaze.png")

    def foc(self, $$0):
        return self.obj.foc($$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)
