import jpype
import jpype.imports

# Auto-generated wrapper for fry
class fryWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fry(*args, **kwargs)

    def acq(self, "textures/entity/skeleton/wither_skeleton.png"):
        return self.obj.acq("textures/entity/skeleton/wither_skeleton.png")

    def fry(self, $$0):
        return self.obj.fry($$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)
