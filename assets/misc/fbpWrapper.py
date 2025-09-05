import jpype
import jpype.imports

# Auto-generated wrapper for fbp
class fbpWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fbp(*args, **kwargs)

    def fbp(self, $$0):
        return self.obj.fbp($$0)

    def c(self, ):
        return fbp.c()

    def fem(self, ):
        return self.obj.fem()

    def fei(self, 0.001F):
        return self.obj.fei(0.001F)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
