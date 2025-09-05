import jpype
import jpype.imports

# Auto-generated wrapper for fsj
class fsjWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fsj(*args, **kwargs)

    def acq(self, "textures/entity/creeper/creeper_armor.png"):
        return self.obj.acq("textures/entity/creeper/creeper_armor.png")

    def fsj(self, fqt<bvo, $$0, $$1):
        return self.obj.fsj(fqt<bvo, $$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()
