import jpype
import jpype.imports

# Auto-generated wrapper for eir
class eirWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eir(*args, **kwargs)

    def a(self, $$0, $$1, $$2):
        return eir.a($$0, $$1, $$2)

    def a(self, Vector3f($$0, $$1, $$2):
        return self.obj.a(Vector3f($$0, $$1, $$2)

    def a(self, $$0):
        return eir.a($$0)

    def a(self, $$0::distanceSquared):
        return self.obj.a($$0::distanceSquared)

    def a(self, $$0):
        return eir.a($$0)

    def sort(self, paramArrayOfVector3f):
        return self.obj.sort(paramArrayOfVector3f)

    def apply(self, param1Vector3f):
        return self.obj.apply(param1Vector3f)
