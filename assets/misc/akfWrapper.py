import jpype
import jpype.imports

# Auto-generated wrapper for akf
class akfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = akf(*args, **kwargs)

    def akf(self, $$0, $$1, $$2):
        return self.obj.akf($$0, $$1, $$2)

    def a(self, $$0):
        return akf.a($$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, BiConsumer<Path, $$2):
        return akf.a($$0, $$1, BiConsumer<Path, $$2)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def ajn(self, $$2, $$0, $$1):
        return self.obj.ajn($$2, $$0, $$1)

    def ajk(self, $$2, $$0, $$1):
        return self.obj.ajk($$2, $$0, $$1)
