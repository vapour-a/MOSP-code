import jpype
import jpype.imports

# Auto-generated wrapper for foo
class fooWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = foo(*args, **kwargs)

    def acq(self, "textures/entity/enderdragon/dragon_fireball.png"):
        return self.obj.acq("textures/entity/enderdragon/dragon_fireball.png")

    def foo(self, $$0):
        return self.obj.foo($$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7):
        return foo.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7)

    def a(self, $$0):
        return self.obj.a($$0)
