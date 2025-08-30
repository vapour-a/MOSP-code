import jpype
import jpype.imports

# Auto-generated wrapper for agk
class agkWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = agk(*args, **kwargs)

    def SimpleCommandExceptionType(self, sw.c("commands.tag.add.failed"):
        return self.obj.SimpleCommandExceptionType(sw.c("commands.tag.add.failed")

    def SimpleCommandExceptionType(self, sw.c("commands.tag.remove.failed"):
        return self.obj.SimpleCommandExceptionType(sw.c("commands.tag.remove.failed")

    def a(self, $$0):
        return agk.a($$0)

    def a(self, (ds):
        return self.obj.a((ds)

    def b(self, (ds):
        return self.obj.b((ds)

    def a(self, (ds):
        return self.obj.a((ds)

    def a(self, $$0):
        return agk.a($$0)

    def a(self, $$0, $$1, $$2):
        return agk.a($$0, $$1, $$2)

    def b(self, $$0, $$1, $$2):
        return agk.b($$0, $$1, $$2)

    def a(self, $$0, $$1):
        return agk.a($$0, $$1)

    def if(self, $$2.isEmpty():
        return self.obj.if($$2.isEmpty()
