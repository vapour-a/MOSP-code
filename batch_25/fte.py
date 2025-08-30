import jpype
import jpype.imports

# Auto-generated wrapper for fte
class fteWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fte(*args, **kwargs)

    def acq(self, "textures/entity/phantom_eyes.png"):
        return self.obj.acq("textures/entity/phantom_eyes.png")

    def fte(self, fqt<T, $$0):
        return self.obj.fte(fqt<T, $$0)

    def a(self, ):
        return self.obj.a()
