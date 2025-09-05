import jpype
import jpype.imports

# Auto-generated wrapper for fbg
class fbgWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fbg(*args, **kwargs)

    def fbg(self, $$0):
        return self.obj.fbg($$0)

    def b(self, ):
        return fbg.b()

    def fem(self, ):
        return self.obj.fem()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, ):
        return self.obj.a()
