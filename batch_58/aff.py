import jpype
import jpype.imports

# Auto-generated wrapper for aff
class affWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = aff(*args, **kwargs)

    def SimpleCommandExceptionType(self, sw.c("commands.op.failed"):
        return self.obj.SimpleCommandExceptionType(sw.c("commands.op.failed")

    def a(self, $$0):
        return aff.a($$0)

    def a(self, (ds):
        return self.obj.a((ds)

    def a(self, $$0, $$1):
        return aff.a($$0, $$1)
