import jpype
import jpype.imports

# Auto-generated wrapper for eod
class eodWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eod(*args, **kwargs)

    def toString(self, ):
        return self.obj.toString()

    def hashCode(self, ):
        return self.obj.hashCode()

    def eod(self, $$0, $$1):
        return self.obj.eod($$0, $$1)

    def equals(self, $$0):
        return self.obj.equals($$0)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def apply(self, param1Vector3f, param1Float1, param1ArrayOfeof, param1Int1, param1Int2, param1Float2):
        return self.obj.apply(param1Vector3f, param1Float1, param1ArrayOfeof, param1Int1, param1Int2, param1Float2)

    def apply(self, param1fee, param1Vector3f):
        return self.obj.apply(param1fee, param1Vector3f)
