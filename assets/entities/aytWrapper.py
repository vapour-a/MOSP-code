import jpype
import jpype.imports

# Auto-generated wrapper for ayt
class aytWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ayt(*args, **kwargs)

    def ayt(self, $$0, $$1):
        return self.obj.ayt($$0, $$1)

    def registerTypes(self, $$0, Map<String, $$1, Map<String, $$2):
        return self.obj.registerTypes($$0, Map<String, $$1, Map<String, $$2)

    def registerBlockEntities(self, $$0):
        return self.obj.registerBlockEntities($$0)
