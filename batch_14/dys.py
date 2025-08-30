import jpype
import jpype.imports

# Auto-generated wrapper for dys
class dysWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dys(*args, **kwargs)

    a = dys.a
    def dys(self, $$0):
        return self.obj.dys($$0)

    def dys(self, $$0, $$1):
        return self.obj.dys($$0, $$1)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def c(self, ):
        return self.obj.c()

    def a(self, $$0):
        return self.obj.a($$0)

    def b(self, ):
        return self.obj.b()
