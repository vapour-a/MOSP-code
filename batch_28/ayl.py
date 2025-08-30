import jpype
import jpype.imports

# Auto-generated wrapper for ayl
class aylWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ayl(*args, **kwargs)

    def ayl(self, $$0, $$1):
        return self.obj.ayl($$0, $$1)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)
