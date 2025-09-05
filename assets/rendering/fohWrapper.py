import jpype
import jpype.imports

# Auto-generated wrapper for foh
class fohWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = foh(*args, **kwargs)

    def acq(self, "textures/entity/horse/donkey.png"):
        return self.obj.acq("textures/entity/horse/donkey.png")

    def acq(self, "textures/entity/horse/mule.png"):
        return self.obj.acq("textures/entity/horse/mule.png")

    def foh(self, $$0, $$1, $$2):
        return self.obj.foh($$0, $$1, $$2)

    def a(self, $$0):
        return self.obj.a($$0)
