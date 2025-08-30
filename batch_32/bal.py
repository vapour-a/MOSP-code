import jpype
import jpype.imports

# Auto-generated wrapper for bal
class balWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bal(*args, **kwargs)

    def d(self, ):
        return self.obj.d()

    def c(self, paramString):
        return self.obj.c(paramString)

    def e(self, ):
        return self.obj.e()
