import jpype
import jpype.imports

# Auto-generated wrapper for cge
class cgeWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cge(*args, **kwargs)

    def cge(self, $$0):
        return self.obj.cge($$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2):
        return cge.a($$0, $$1, $$2)

    def eed(self, 7.0D, 7.0D, 7.0D, 7.0D, 7.0D, 7.0D):
        return self.obj.eed(7.0D, 7.0D, 7.0D, 7.0D, 7.0D, 7.0D)
