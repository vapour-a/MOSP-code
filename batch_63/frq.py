import jpype
import jpype.imports

# Auto-generated wrapper for frq
class frqWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = frq(*args, **kwargs)

    def acq(self, "textures/entity/horse/horse_zombie.png"):
        return self.obj.acq("textures/entity/horse/horse_zombie.png")

    def acq(self, "textures/entity/horse/horse_skeleton.png"):
        return self.obj.acq("textures/entity/horse/horse_skeleton.png")

    def frq(self, $$0, $$1):
        return self.obj.frq($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)
