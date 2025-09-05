import jpype
import jpype.imports

# Auto-generated wrapper for fov
class fovWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fov(*args, **kwargs)

    def acq(self, "textures/entity/endermite.png"):
        return self.obj.acq("textures/entity/endermite.png")

    def fov(self, $$0):
        return self.obj.fov($$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def b(self, $$0):
        return self.obj.b($$0)
