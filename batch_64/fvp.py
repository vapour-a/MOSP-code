import jpype
import jpype.imports

# Auto-generated wrapper for fvp
class fvpWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fvp(*args, **kwargs)

    def acq(self, "textures/colormap/grass.png"):
        return self.obj.acq("textures/colormap/grass.png")

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def IllegalStateException(self, texture", $$2):
        return self.obj.IllegalStateException(texture", $$2)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)
