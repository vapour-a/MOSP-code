import jpype
import jpype.imports

# Auto-generated wrapper for ewf
class ewfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ewf(*args, **kwargs)

    def acq(self, "textures/gui/container/dispenser.png"):
        return self.obj.acq("textures/gui/container/dispenser.png")

    def ewf(self, $$0, $$1, $$2):
        return self.obj.ewf($$0, $$1, $$2)

    def b(self, ):
        return self.obj.b()

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)
