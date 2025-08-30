import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def a(self, ):
        return self.obj.a()

    def a(self, paramUUID, paramb):
        return self.obj.a(paramUUID, paramb)

    def a(self, paramsf):
        return self.obj.a(paramsf)
