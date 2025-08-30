import jpype
import jpype.imports

# Auto-generated wrapper for exa
class exaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = exa(*args, **kwargs)

    def acq(self, "textures/gui/container/smoker.png"):
        return self.obj.acq("textures/gui/container/smoker.png")

    def exa(self, $$0, $$1, $$2):
        return self.obj.exa($$0, $$1, $$2)

    def eyk(self, ):
        return self.obj.eyk()
