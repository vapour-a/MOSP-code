import jpype
import jpype.imports

# Auto-generated wrapper for fai
class faiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fai(*args, **kwargs)

    def fai(self, $$0):
        return self.obj.fai($$0)

    def c(self, ):
        return fai.c()

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def b(self, ):
        return self.obj.b()

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
