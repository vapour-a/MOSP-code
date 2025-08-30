import jpype
import jpype.imports

# Auto-generated wrapper for avs
class avsWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = avs(*args, **kwargs)

    def avs(self, $$0, $$1, Function<String, $$2):
        return self.obj.avs($$0, $$1, Function<String, $$2)

    def a(self, $$0):
        return self.obj.a($$0)
