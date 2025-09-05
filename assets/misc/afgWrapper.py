import jpype
import jpype.imports

# Auto-generated wrapper for afg
class afgWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = afg(*args, **kwargs)

    def SimpleCommandExceptionType(self, sw.c("commands.pardon.failed"):
        return self.obj.SimpleCommandExceptionType(sw.c("commands.pardon.failed")

    def a(self, $$0):
        return afg.a($$0)

    def a(self, (ds):
        return self.obj.a((ds)

    def a(self, $$0, $$1):
        return afg.a($$0, $$1)
