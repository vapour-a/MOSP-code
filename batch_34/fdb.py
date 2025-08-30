import jpype
import jpype.imports

# Auto-generated wrapper for fdb
class fdbWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fdb(*args, **kwargs)

    def fdb(self, $$0):
        return self.obj.fdb($$0)

    def a(self, ):
        return fdb.a()

    def fem(self, ):
        return self.obj.fem()

    def b(self, ):
        return fdb.b()

    def fei(self, 0.25F):
        return self.obj.fei(0.25F)

    def c(self, ):
        return fdb.c()

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7)
