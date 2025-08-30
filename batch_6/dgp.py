import jpype
import jpype.imports

# Auto-generated wrapper for dgp
class dgpWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dgp(*args, **kwargs)

    def a(self, paramcmm):
        return self.obj.a(paramcmm)

    def a(self, ):
        return self.obj.a()
