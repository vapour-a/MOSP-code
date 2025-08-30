import jpype
import jpype.imports

# Auto-generated wrapper for gg
class ggWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = gg(*args, **kwargs)

    def a(self, paramT, paramsf):
        return self.obj.a(paramT, paramsf)

    def b(self, paramsf):
        return self.obj.b(paramsf)

    def a(self, paramT, paramJsonObject):
        return self.obj.a(paramT, paramJsonObject)

    def a(self, paramA):
        return self.obj.a(paramA)

    def b(self, param1dm):
        return self.obj.b(param1dm)

    def a(self, ):
        return self.obj.a()
