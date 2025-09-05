import jpype
import jpype.imports

# Auto-generated wrapper for azv
class azvWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = azv(*args, **kwargs)

    def azv(self, $$0, $$1):
        return self.obj.azv($$0, $$1)

    def a(self, $$0, Map<String, $$1, $$2):
        return azv.a($$0, Map<String, $$1, $$2)

    def b(self, $$0, Map<String, $$1, $$2):
        return azv.b($$0, Map<String, $$1, $$2)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)

    def registerTypes(self, $$0, Map<String, $$1, Map<String, $$2):
        return self.obj.registerTypes($$0, Map<String, $$1, Map<String, $$2)

    def apply(self, $$0, $$1):
        return self.obj.apply($$0, $$1)

    def Dynamic(self, $$0, $$1):
        return self.obj.Dynamic($$0, $$1)
