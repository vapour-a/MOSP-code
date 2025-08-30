import jpype
import jpype.imports

# Auto-generated wrapper for epk
class epkWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = epk(*args, **kwargs)

    def acq(self, "textures/gui/checkbox.png"):
        return self.obj.acq("textures/gui/checkbox.png")

    def epk(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.epk($$0, $$1, $$2, $$3, $$4, $$5)

    def epk(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6):
        return self.obj.epk($$0, $$1, $$2, $$3, $$4, $$5, $$6)

    def c(self, ):
        return self.obj.c()

    def a(self, ):
        return self.obj.a()

    def a(self, $$0):
        return self.obj.a($$0)

    def b(self, $$0, $$1, $$2, $$3):
        return self.obj.b($$0, $$1, $$2, $$3)
