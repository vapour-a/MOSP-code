import jpype
import jpype.imports

# Auto-generated wrapper for ewj
class ewjWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ewj(*args, **kwargs)

    def acq(self, "textures/gui/container/furnace.png"):
        return self.obj.acq("textures/gui/container/furnace.png")

    def ewj(self, $$0, $$1, $$2):
        return self.obj.ewj($$0, $$1, $$2)

    def eyj(self, ):
        return self.obj.eyj()
