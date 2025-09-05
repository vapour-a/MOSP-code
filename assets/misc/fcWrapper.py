import jpype
import jpype.imports

# Auto-generated wrapper for fc
class fcWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fc(*args, **kwargs)

    def SimpleCommandExceptionType(self, sw.c("argument.uuid.invalid"):
        return self.obj.SimpleCommandExceptionType(sw.c("argument.uuid.invalid")

    def a(self, $$0, $$1):
        return fc.a($$0, $$1)

    def a(self, ):
        return fc.a()

    def fc(self, ):
        return self.obj.fc()

    def a(self, $$0):
        return self.obj.a($$0)

    def getExamples(self, ):
        return self.obj.getExamples()
