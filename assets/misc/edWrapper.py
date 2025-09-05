import jpype
import jpype.imports

# Auto-generated wrapper for ed
class edWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ed(*args, **kwargs)

    def DynamicCommandExceptionType(self, sw.a("argument.gamemode.invalid", }):
        return self.obj.DynamicCommandExceptionType(sw.a("argument.gamemode.invalid", })

    def a(self, $$0):
        return self.obj.a($$0)

    def listSuggestions(self, $$0, $$1):
        return self.obj.listSuggestions($$0, $$1)

    def getExamples(self, ):
        return self.obj.getExamples()

    def a(self, ):
        return ed.a()

    def ed(self, ):
        return self.obj.ed()

    def a(self, $$0, $$1):
        return ed.a($$0, $$1)
