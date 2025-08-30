import jpype
import jpype.imports

# Auto-generated wrapper for deo
class deoWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = deo(*args, **kwargs)

    def a(self, paramT):
        return self.obj.a(paramT)

    def a(self, paramPredicate):
        return self.obj.a(paramPredicate)

    def a(self, paramInt):
        return self.obj.a(paramInt)

    def a(self, paramsf):
        return self.obj.a(paramsf)

    def b(self, paramsf):
        return self.obj.b(paramsf)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def c(self, ):
        return self.obj.c()

    def create(self, param1Int, param1hj, param1dep, param1List):
        return self.obj.create(param1Int, param1hj, param1dep, param1List)
