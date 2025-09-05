import jpype
import jpype.imports

# Auto-generated wrapper for fcw
class fcwWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fcw(*args, **kwargs)

    def fcw(self, $$0):
        return self.obj.fcw($$0)

    def a(self, ):
        return fcw.a()

    def fem(self, ):
        return self.obj.fem()

    def b(self, ):
        return self.obj.b()

    def c(self, ):
        return self.obj.c()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7)
