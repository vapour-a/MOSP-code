import jpype
import jpype.imports

# Auto-generated wrapper for azu
class azuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = azu(*args, **kwargs)

    def azu(self, $$0, $$1):
        return self.obj.azu($$0, $$1)

    def a(self, $$0, Map<String, $$1, $$2):
        return azu.a($$0, Map<String, $$1, $$2)

    def getChoiceType(self, $$0, $$1):
        return self.obj.getChoiceType($$0, $$1)

    def registerBlockEntities(self, $$0):
        return self.obj.registerBlockEntities($$0)

    def registerTypes(self, $$0, Map<String, $$1, Map<String, $$2):
        return self.obj.registerTypes($$0, Map<String, $$1, Map<String, $$2)

    def apply(self, $$0, $$1):
        return self.obj.apply($$0, $$1)

    def Dynamic(self, $$0, $$1):
        return self.obj.Dynamic($$0, $$1)
