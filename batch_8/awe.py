import jpype
import jpype.imports

# Auto-generated wrapper for awe
class aweWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = awe(*args, **kwargs)

    def awe(self, $$0, $$1, $$2):
        return self.obj.awe($$0, $$1, $$2)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, paramString, paramDynamic):
        return self.obj.a(paramString, paramDynamic)
