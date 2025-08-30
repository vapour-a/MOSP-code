import jpype
import jpype.imports

# Auto-generated wrapper for fao
class faoWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fao(*args, **kwargs)

    def fao(self, $$0):
        return self.obj.fao($$0)

    def a(self, ):
        return fao.a()

    def fem(self, ):
        return self.obj.fem()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7)

    def b(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7):
        return self.obj.b($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)
