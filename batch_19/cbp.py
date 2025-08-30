import jpype
import jpype.imports

# Auto-generated wrapper for cbp
class cbpWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cbp(*args, **kwargs)

    def a(self, paramInt):
        return self.obj.a(paramInt)

    def a(self, paramInt1, paramInt2):
        return self.obj.a(paramInt1, paramInt2)

    def a(self, ):
        return self.obj.a()
