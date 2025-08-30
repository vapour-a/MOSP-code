import jpype
import jpype.imports

# Auto-generated wrapper for dx
class dxWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dx(*args, **kwargs)

    def DynamicCommandExceptionType(self, sw.a("argument.color.invalid", }):
        return self.obj.DynamicCommandExceptionType(sw.a("argument.color.invalid", })

    def a(self, ):
        return dx.a()

    def dx(self, ):
        return self.obj.dx()

    def a(self, $$0, $$1):
        return dx.a($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def listSuggestions(self, $$0, $$1):
        return self.obj.listSuggestions($$0, $$1)

    def getExamples(self, ):
        return self.obj.getExamples()
