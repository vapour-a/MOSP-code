import jpype
import jpype.imports

# Auto-generated wrapper for dpu
class dpuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dpu(*args, **kwargs)

    def a(self, $$0):
        return self.obj.a($$0)

    def dpu(self, $$0, $$1, $$2):
        return self.obj.dpu($$0, $$1, $$2)

    def a(self, ):
        return self.obj.a()

    def a(self, $$0, BiConsumer<gu, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, BiConsumer<gu, $$1, $$2, $$3, $$4, $$5)
