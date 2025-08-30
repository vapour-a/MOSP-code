import jpype
import jpype.imports

# Auto-generated wrapper for fay
class fayWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fay(*args, **kwargs)

    def fay(self, $$0):
        return self.obj.fay($$0)

    def c(self, ):
        return fay.c()

    def fem(self, ):
        return self.obj.fem()

    def d(self, ):
        return self.obj.d()
