import jpype
import jpype.imports

# Auto-generated wrapper for bcp
class bcpWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bcp(*args, **kwargs)

    def close(self, ):
        return self.obj.close()

    def b(self, bcp<Source>, $$0):
        return self.obj.b(bcp<Source>, $$0)

    def c(self, bcp<Either<Source, Exception>>, $$0):
        return self.obj.c(bcp<Either<Source, Exception>>, $$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def bn(self, ):
        return self.obj.bn()

    def a(self, $$0):
        return self.obj.a($$0)

    def toString(self, ):
        return self.obj.toString()

    def bn(self, ):
        return self.obj.bn()

    def a(self, paramMsg):
        return self.obj.a(paramMsg)
