import jpype
import jpype.imports

# Auto-generated wrapper for afv
class afvWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = afv(*args, **kwargs)

    def SimpleCommandExceptionType(self, sw.c("commands.save.alreadyOn"):
        return self.obj.SimpleCommandExceptionType(sw.c("commands.save.alreadyOn")

    def a(self, $$0):
        return afv.a($$0)
