import jpype
import jpype.imports

# Auto-generated wrapper for ia
class iaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ia(*args, **kwargs)

    def b(self, paramInt, paramacp, paramT, paramLifecycle):
        return self.obj.b(paramInt, paramacp, paramT, paramLifecycle)

    def a(self, paramacp, paramT, paramLifecycle):
        return self.obj.a(paramacp, paramT, paramLifecycle)

    def k(self, ):
        return self.obj.k()

    def n(self, ):
        return self.obj.n()
