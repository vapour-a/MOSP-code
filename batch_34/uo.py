import jpype
import jpype.imports

# Auto-generated wrapper for uo
class uoWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = uo(*args, **kwargs)

    def a(self, paramsf):
        return self.obj.a(paramsf)

    def a(self, paramT):
        return self.obj.a(paramT)

    def b(self, ):
        return self.obj.b()
