import jpype
import jpype.imports

# Auto-generated wrapper for fpa
class fpaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fpa(*args, **kwargs)

    def acq(self, "textures/entity/illager/evoker_fangs.png"):
        return self.obj.acq("textures/entity/illager/evoker_fangs.png")

    def fpa(self, $$0):
        return self.obj.fpa($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0):
        return self.obj.a($$0)
