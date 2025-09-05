import jpype
import jpype.imports

# Auto-generated wrapper for ew
class ewWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ew(*args, **kwargs)

    def DynamicCommandExceptionType(self, sw.a("slot.unknown", }):
        return self.obj.DynamicCommandExceptionType(sw.a("slot.unknown", })

    def a(self, ):
        return ew.a()

    def ew(self, ):
        return self.obj.ew()

    def a(self, $$0, $$1):
        return ew.a($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def listSuggestions(self, $$0, $$1):
        return self.obj.listSuggestions($$0, $$1)

    def getExamples(self, ):
        return self.obj.getExamples()
