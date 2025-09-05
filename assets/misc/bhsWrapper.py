import jpype
import jpype.imports

# Auto-generated wrapper for bhs
class bhsWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bhs(*args, **kwargs)

    def a(self, ):
        return self.obj.a()

    def e(self, paramaif, paramE, paramLong):
        return self.obj.e(paramaif, paramE, paramLong)

    def f(self, paramaif, paramE, paramLong):
        return self.obj.f(paramaif, paramE, paramLong)

    def g(self, paramaif, paramE, paramLong):
        return self.obj.g(paramaif, paramE, paramLong)

    def b(self, ):
        return self.obj.b()
