import jpype
import jpype.imports

# Auto-generated wrapper for k
class kWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = k(*args, **kwargs)

    def b(self, paramT):
        return self.obj.b(paramT)

    def b(self, paramDouble):
        return self.obj.b(paramDouble)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
