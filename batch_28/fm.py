import jpype
import jpype.imports

# Auto-generated wrapper for fm
class fmWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fm(*args, **kwargs)

    def SimpleCommandExceptionType(self, sw.c("argument.rotation.incomplete"):
        return self.obj.SimpleCommandExceptionType(sw.c("argument.rotation.incomplete")

    def a(self, ):
        return fm.a()

    def fm(self, ):
        return self.obj.fm()

    def a(self, $$0, $$1):
        return fm.a($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def fr(self, $$3, $$2, fq(true, 0.0D):
        return self.obj.fr($$3, $$2, fq(true, 0.0D)

    def getExamples(self, ):
        return self.obj.getExamples()
