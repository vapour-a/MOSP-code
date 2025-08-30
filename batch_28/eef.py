import jpype
import jpype.imports

# Auto-generated wrapper for eef
class eefWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eef(*args, **kwargs)

    def eef(self, $$0):
        return self.obj.eef($$0)

    def eef(self, $$0, $$1):
        return self.obj.eef($$0, $$1)

    def a(self, ):
        return self.obj.a()

    def c(self, ):
        return self.obj.c()
