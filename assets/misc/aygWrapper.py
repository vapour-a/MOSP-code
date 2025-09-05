import jpype
import jpype.imports

# Auto-generated wrapper for ayg
class aygWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ayg(*args, **kwargs)

    def ayg(self, $$0, $$1):
        return self.obj.ayg($$0, $$1)

    def a(self, $$0):
        return ayg.a($$0)

    def a(self, $$0, Map<String, $$1, $$2):
        return ayg.a($$0, Map<String, $$1, $$2)

    def a(self, $$0):
        return self.obj.a($$0)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)
