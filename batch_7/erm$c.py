import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def toString(self, ):
        return self.obj.toString()

    def hashCode(self, ):
        return self.obj.hashCode()

    def equals(self, $$0):
        return self.obj.equals($$0)

    def c(self, $$0):
        return self.obj.c($$0)

    def a(self, ):
        return self.obj.a()
