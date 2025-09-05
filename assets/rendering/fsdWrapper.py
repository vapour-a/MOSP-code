import jpype
import jpype.imports

# Auto-generated wrapper for fsd
class fsdWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fsd(*args, **kwargs)

    def acq(self, "textures/entity/zombie_villager/zombie_villager.png"):
        return self.obj.acq("textures/entity/zombie_villager/zombie_villager.png")

    def fsd(self, $$0):
        return self.obj.fsd($$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def b(self, $$0):
        return self.obj.b($$0)
