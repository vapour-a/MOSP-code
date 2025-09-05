import jpype
import jpype.imports

# Auto-generated wrapper for aee
class aeeWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = aee(*args, **kwargs)

    def SimpleCommandExceptionType(self, sw.c("commands.deop.failed"):
        return self.obj.SimpleCommandExceptionType(sw.c("commands.deop.failed")

    def a(self, $$0):
        return aee.a($$0)

    def a(self, (ds):
        return self.obj.a((ds)

    def a(self, $$0, $$1):
        return aee.a($$0, $$1)
