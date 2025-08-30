import jpype
import jpype.imports

# Auto-generated wrapper for arf
class arfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = arf(*args, **kwargs)

    def arf(self, $$0, $$1):
        return self.obj.arf($$0, $$1)

    def makeRule(self, ):
        return self.obj.makeRule()

    def b(self, $$0, $$1, Function<String, $$2):
        return arf.b($$0, $$1, Function<String, $$2)

    def arf(self, $$0, $$1, $$2):
        return self.obj.arf($$0, $$1, $$2)

    def a(self, $$0):
        return self.obj.a($$0)
