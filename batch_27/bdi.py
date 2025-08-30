import jpype
import jpype.imports

# Auto-generated wrapper for bdi
class bdiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bdi(*args, **kwargs)

    def bdi(self, $$0, $$1):
        return self.obj.bdi($$0, $$1)

    def a(self, $$0, $$1):
        return bdi.a($$0, $$1)

    def bdi(self, $$0, $$1):
        return self.obj.bdi($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def c(self, ):
        return self.obj.c()

    def toString(self, ):
        return self.obj.toString()
