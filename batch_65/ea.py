import jpype
import jpype.imports

# Auto-generated wrapper for ea
class eaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ea(*args, **kwargs)

    def DynamicCommandExceptionType(self, sw.a("argument.dimension.invalid", }):
        return self.obj.DynamicCommandExceptionType(sw.a("argument.dimension.invalid", })

    def a(self, $$0):
        return self.obj.a($$0)

    def listSuggestions(self, $$0, $$1):
        return self.obj.listSuggestions($$0, $$1)

    def getExamples(self, ):
        return self.obj.getExamples()

    def a(self, ):
        return ea.a()

    def ea(self, ):
        return self.obj.ea()

    def a(self, $$0, $$1):
        return ea.a($$0, $$1)
