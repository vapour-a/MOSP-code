import jpype
import jpype.imports

# Auto-generated wrapper for ayj
class ayjWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ayj(*args, **kwargs)

    def ayj(self, $$0, $$1):
        return self.obj.ayj($$0, $$1)

    def a(self, $$0, Map<String, $$1, $$2):
        return ayj.a($$0, Map<String, $$1, $$2)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)

    def registerBlockEntities(self, $$0):
        return self.obj.registerBlockEntities($$0)
