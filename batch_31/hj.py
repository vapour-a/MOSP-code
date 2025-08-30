import jpype
import jpype.imports

# Auto-generated wrapper for hj
class hjWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = hj(*args, **kwargs)

    def a(self, paramT):
        return self.obj.a(paramT)

    def a(self, paramInt):
        return self.obj.a(paramInt)

    def b(self, $$0):
        return self.obj.b($$0)

    def IllegalArgumentException(self, $$0):
        return self.obj.IllegalArgumentException($$0)

    def b(self, ):
        return self.obj.b()
