import jpype
import jpype.imports

# Auto-generated wrapper for evu
class evuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = evu(*args, **kwargs)

    def acq(self, "textures/gui/container/blast_furnace.png"):
        return self.obj.acq("textures/gui/container/blast_furnace.png")

    def evu(self, $$0, $$1, $$2):
        return self.obj.evu($$0, $$1, $$2)

    def exz(self, ):
        return self.obj.exz()
