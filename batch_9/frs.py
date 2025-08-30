import jpype
import jpype.imports

# Auto-generated wrapper for frs
class frsWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = frs(*args, **kwargs)

    def acq(self, "textures/entity/villager/villager.png"):
        return self.obj.acq("textures/entity/villager/villager.png")

    def frs(self, $$0):
        return self.obj.frs($$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)
