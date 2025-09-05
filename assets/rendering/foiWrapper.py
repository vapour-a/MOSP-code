import jpype
import jpype.imports

# Auto-generated wrapper for foi
class foiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = foi(*args, **kwargs)

    def acq(self, "textures/entity/chicken.png"):
        return self.obj.acq("textures/entity/chicken.png")

    def foi(self, $$0):
        return self.obj.foi($$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
