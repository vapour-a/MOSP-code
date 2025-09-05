import jpype
import jpype.imports

# Auto-generated wrapper for gz
class gzWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = gz(*args, **kwargs)

    def b(self, paramT):
        return self.obj.b(paramT)

    def a(self, paramacq):
        return self.obj.a(paramacq)

    def a(self, paramInt):
        return self.obj.a(paramInt)

    def a(self, ):
        return self.obj.a()
