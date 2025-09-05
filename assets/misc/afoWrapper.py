import jpype
import jpype.imports

# Auto-generated wrapper for afo
class afoWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = afo(*args, **kwargs)

    def SimpleCommandExceptionType(self, sw.c("commands.recipe.give.failed"):
        return self.obj.SimpleCommandExceptionType(sw.c("commands.recipe.give.failed")

    def SimpleCommandExceptionType(self, sw.c("commands.recipe.take.failed"):
        return self.obj.SimpleCommandExceptionType(sw.c("commands.recipe.take.failed")

    def a(self, $$0):
        return afo.a($$0)

    def a(self, (ds):
        return self.obj.a((ds)

    def a(self, (ds):
        return self.obj.a((ds)

    def b(self, (ds):
        return self.obj.b((ds)

    def b(self, (ds):
        return self.obj.b((ds)

    def a(self, $$0, $$1, $$2):
        return afo.a($$0, $$1, $$2)

    def b(self, $$0, $$1, $$2):
        return afo.b($$0, $$1, $$2)
