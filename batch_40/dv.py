import jpype
import jpype.imports

# Auto-generated wrapper for dv
class dvWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dv(*args, **kwargs)

    def SimpleCommandExceptionType(self, sw.c("argument.angle.incomplete"):
        return self.obj.SimpleCommandExceptionType(sw.c("argument.angle.incomplete")

    def SimpleCommandExceptionType(self, sw.c("argument.angle.invalid"):
        return self.obj.SimpleCommandExceptionType(sw.c("argument.angle.invalid")

    def a(self, ):
        return dv.a()

    def dv(self, ):
        return self.obj.dv()

    def a(self, $$0, $$1):
        return dv.a($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$2, $$1):
        return self.obj.a($$2, $$1)

    def getExamples(self, ):
        return self.obj.getExamples()

    def a(self, $$0):
        return self.obj.a($$0)
