import jpype
import jpype.imports

# Auto-generated wrapper for ej
class ejWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ej(*args, **kwargs)

    def DynamicCommandExceptionType(self, sw.a("arguments.objective.notFound", }):
        return self.obj.DynamicCommandExceptionType(sw.a("arguments.objective.notFound", })

    def DynamicCommandExceptionType(self, sw.a("arguments.objective.readonly", }):
        return self.obj.DynamicCommandExceptionType(sw.a("arguments.objective.readonly", })

    def a(self, ):
        return ej.a()

    def ej(self, ):
        return self.obj.ej()

    def a(self, $$0, $$1):
        return ej.a($$0, $$1)

    def b(self, $$0, $$1):
        return ej.b($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def listSuggestions(self, $$0, $$1):
        return self.obj.listSuggestions($$0, $$1)

    def getExamples(self, ):
        return self.obj.getExamples()
