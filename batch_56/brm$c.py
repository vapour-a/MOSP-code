import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def i(self, ):
        return self.obj.i()
