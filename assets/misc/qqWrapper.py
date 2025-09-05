import jpype
import jpype.imports

# Auto-generated wrapper for qq
class qqWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = qq(*args, **kwargs)

    def d(self, paramInt, paramT):
        return self.obj.d(paramInt, paramT)

    def c(self, paramInt, paramT):
        return self.obj.c(paramInt, paramT)

    def c(self, paramInt):
        return self.obj.c(paramInt)

    def a(self, paramInt, paramrk):
        return self.obj.a(paramInt, paramrk)

    def b(self, paramInt, paramrk):
        return self.obj.b(paramInt, paramrk)

    def f(self, ):
        return self.obj.f()
