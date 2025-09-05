import jpype
import jpype.imports

# Auto-generated wrapper for evx
class evxWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = evx(*args, **kwargs)

    def acq(self, "textures/gui/container/brewing_stand.png"):
        return self.obj.acq("textures/gui/container/brewing_stand.png")

    def evx(self, $$0, $$1, $$2):
        return self.obj.evx($$0, $$1, $$2)

    def b(self, ):
        return self.obj.b()

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)
