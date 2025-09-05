import jpype
import jpype.imports

# Auto-generated wrapper for azf
class azfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = azf(*args, **kwargs)

    def azf(self, $$0, $$1):
        return self.obj.azf($$0, $$1)

    def a(self, $$0, Map<String, $$1, $$2):
        return azf.a($$0, Map<String, $$1, $$2)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)
