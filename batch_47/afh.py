import jpype
import jpype.imports

# Auto-generated wrapper for afh
class afhWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = afh(*args, **kwargs)

    def SimpleCommandExceptionType(self, sw.c("commands.pardonip.invalid"):
        return self.obj.SimpleCommandExceptionType(sw.c("commands.pardonip.invalid")

    def SimpleCommandExceptionType(self, sw.c("commands.pardonip.failed"):
        return self.obj.SimpleCommandExceptionType(sw.c("commands.pardonip.failed")

    def a(self, $$0):
        return afh.a($$0)

    def a(self, (ds):
        return self.obj.a((ds)

    def a(self, $$0, $$1):
        return afh.a($$0, $$1)
