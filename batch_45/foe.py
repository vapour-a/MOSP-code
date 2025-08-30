import jpype
import jpype.imports

# Auto-generated wrapper for foe
class foeWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = foe(*args, **kwargs)

    def acq(self, "textures/entity/camel/camel.png"):
        return self.obj.acq("textures/entity/camel/camel.png")

    def foe(self, $$0, $$1):
        return self.obj.foe($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)
