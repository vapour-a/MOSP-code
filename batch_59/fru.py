import jpype
import jpype.imports

# Auto-generated wrapper for fru
class fruWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fru(*args, **kwargs)

    def acq(self, "textures/entity/wandering_trader.png"):
        return self.obj.acq("textures/entity/wandering_trader.png")

    def fru(self, $$0):
        return self.obj.fru($$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)
