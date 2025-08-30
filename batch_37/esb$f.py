import jpype
import jpype.imports

# Auto-generated wrapper for f
class fWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = f(*args, **kwargs)

    def a(self, paramInt):
        return self.obj.a(paramInt)

    def a(self, ):
        return self.obj.a()

    def c(self, ):
        return self.obj.c()

    def d(self, ):
        return self.obj.d()
