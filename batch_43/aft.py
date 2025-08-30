import jpype
import jpype.imports

# Auto-generated wrapper for aft
class aftWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = aft(*args, **kwargs)

    def SimpleCommandExceptionType(self, sw.c("commands.save.failed"):
        return self.obj.SimpleCommandExceptionType(sw.c("commands.save.failed")

    def a(self, $$0):
        return aft.a($$0)

    def a(self, (ds):
        return self.obj.a((ds)

    def a(self, (ds):
        return self.obj.a((ds)

    def a(self, $$0, $$1):
        return aft.a($$0, $$1)
