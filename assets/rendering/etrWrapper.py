import jpype
import jpype.imports

# Auto-generated wrapper for etr
class etrWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = etr(*args, **kwargs)

    def acq(self, "textures/gui/demo_background.png"):
        return self.obj.acq("textures/gui/demo_background.png")

    def etr(self, ):
        return self.obj.etr()

    def b(self, ):
        return self.obj.b()

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)
