import jpype
import jpype.imports

# Auto-generated wrapper for lj
class ljWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = lj(*args, **kwargs)

    def lj(self, $$0, $$1):
        return self.obj.lj($$0, $$1)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, BiConsumer<acq, $$1):
        return self.obj.a($$0, BiConsumer<acq, $$1)

    def a(self, $$0, $$1, BiConsumer<acq, $$2):
        return self.obj.a($$0, $$1, BiConsumer<acq, $$2)

    def a(self, Function<cpn, $$0, $$1):
        return lj.a(Function<cpn, $$0, $$1)

    def lj(self, $$0.apply($$2):
        return self.obj.lj($$0.apply($$2)

    def a(self, $$0):
        return lj.a($$0)

    def lj(self, lh.b($$0):
        return self.obj.lj(lh.b($$0)

    def get(self, param1cpn):
        return self.obj.get(param1cpn)

    def create(self, $$0, BiConsumer<acq, $$1):
        return self.obj.create($$0, BiConsumer<acq, $$1)

    def get(self, $$0):
        return self.obj.get($$0)

    def createWithSuffix(self, $$0, $$1, BiConsumer<acq, $$2):
        return self.obj.createWithSuffix($$0, $$1, BiConsumer<acq, $$2)

    def get(self, $$0):
        return self.obj.get($$0)

    def updateTexture(self, $$0):
        return self.obj.updateTexture($$0)

    def get(self, $$1):
        return self.obj.get($$1)
