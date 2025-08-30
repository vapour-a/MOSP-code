import jpype
import jpype.imports

# Auto-generated wrapper for crf
class crfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = crf(*args, **kwargs)

    def Object2IntOpenHashMap(self, ):
        return self.obj.Object2IntOpenHashMap()

    def crf(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.crf($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0, $$1, $$2, $$3, $$4):
        return self.obj.a($$0, $$1, $$2, $$3, $$4)

    def c(self, $$0, $$1, $$2):
        return self.obj.c($$0, $$1, $$2)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def c(self, $$0, $$1, $$2, $$3):
        return self.obj.c($$0, $$1, $$2, $$3)

    def a(self, $$0):
        return crf.a($$0)

    def g(self, $$0):
        return self.obj.g($$0)

    def c_(self, $$0):
        return self.obj.c_($$0)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
