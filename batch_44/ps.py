import jpype
import jpype.imports

# Auto-generated wrapper for ps
class psWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ps(*args, **kwargs)

    def a(self, parampr):
        return self.obj.a(parampr)

    def b(self, parampr):
        return self.obj.b(parampr)

    def c(self, parampr):
        return self.obj.c(parampr)
