import jpype
import jpype.imports

# Auto-generated wrapper for bgy
class bgyWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bgy(*args, **kwargs)

    def a(self, paramT):
        return self.obj.a(paramT)

    def c(self, ):
        return self.obj.c()
