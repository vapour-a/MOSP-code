import jpype
import jpype.imports

# Auto-generated wrapper for bju
class bjuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bju(*args, **kwargs)

    def a(self, $$0, $$1, $$2, $$3):
        return bju.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1, $$2, $$3, eei::c):
        return self.obj.a($$0, $$1, $$2, $$3, eei::c)

    def b(self, $$0, $$1, $$2, $$3):
        return bju.b($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1, $$2, $$3, bfj::dg):
        return self.obj.a($$0, $$1, $$2, $$3, bfj::dg)

    def a(self, $$0, $$1, $$2, $$3, Function<T, $$4):
        return self.obj.a($$0, $$1, $$2, $$3, Function<T, $$4)
