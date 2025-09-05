import jpype
import jpype.imports

# Auto-generated wrapper for dpv
class dpvWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dpv(*args, **kwargs)

    def a(self, $$0):
        return self.obj.a($$0)

    def dpv(self, $$0, $$1, $$2):
        return self.obj.dpv($$0, $$1, $$2)

    def a(self, ):
        return self.obj.a()

    def a(self, $$0, BiConsumer<gu, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, BiConsumer<gu, $$1, $$2, $$3, $$4, $$5)
