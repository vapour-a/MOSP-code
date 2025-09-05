import jpype
import jpype.imports

# Auto-generated wrapper for frb
class frbWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = frb(*args, **kwargs)

    def acq(self, "textures/entity/sniffer/sniffer.png"):
        return self.obj.acq("textures/entity/sniffer/sniffer.png")

    def frb(self, $$0):
        return self.obj.frb($$0)

    def a(self, $$0):
        return self.obj.a($$0)
