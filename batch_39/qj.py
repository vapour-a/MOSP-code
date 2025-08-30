import jpype
import jpype.imports

# Auto-generated wrapper for qj
class qjWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = qj(*args, **kwargs)

    def a(self, $$0):
        return self.obj.a($$0)

    def CommandSyntaxException(self, SimpleCommandExceptionType($$3):
        return self.obj.CommandSyntaxException(SimpleCommandExceptionType($$3)

    def a(self, ):
        return qj.a()

    def qj(self, ):
        return self.obj.qj()

    def a(self, $$0, $$1):
        return qj.a($$0, $$1)

    def listSuggestions(self, $$0, $$1):
        return self.obj.listSuggestions($$0, $$1)

    def getExamples(self, ):
        return self.obj.getExamples()
