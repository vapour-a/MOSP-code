import jpype
import jpype.imports

# Auto-generated wrapper for qg
class qgWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = qg(*args, **kwargs)

    def a(self, $$0):
        return self.obj.a($$0)

    def CommandSyntaxException(self, SimpleCommandExceptionType($$2):
        return self.obj.CommandSyntaxException(SimpleCommandExceptionType($$2)

    def a(self, ):
        return qg.a()

    def qg(self, ):
        return self.obj.qg()

    def a(self, $$0, $$1):
        return qg.a($$0, $$1)

    def listSuggestions(self, $$0, $$1):
        return self.obj.listSuggestions($$0, $$1)

    def getExamples(self, ):
        return self.obj.getExamples()
