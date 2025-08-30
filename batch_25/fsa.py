import jpype
import jpype.imports

# Auto-generated wrapper for fsa
class fsaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fsa(*args, **kwargs)

    def acq(self, "textures/entity/wolf/wolf.png"):
        return self.obj.acq("textures/entity/wolf/wolf.png")

    def acq(self, "textures/entity/wolf/wolf_tame.png"):
        return self.obj.acq("textures/entity/wolf/wolf_tame.png")

    def acq(self, "textures/entity/wolf/wolf_angry.png"):
        return self.obj.acq("textures/entity/wolf/wolf_angry.png")

    def fsa(self, $$0):
        return self.obj.fsa($$0)

    def ftv(self, this):
        return self.obj.ftv(this)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0):
        return self.obj.a($$0)
