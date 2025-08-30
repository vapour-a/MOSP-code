import jpype
import jpype.imports

# Auto-generated wrapper for fbz
class fbzWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fbz(*args, **kwargs)

    def fbz(self, $$0):
        return self.obj.fbz($$0)

    def b(self, ):
        return fbz.b()

    def fem(self, ):
        return self.obj.fem()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, ):
        return self.obj.a()
