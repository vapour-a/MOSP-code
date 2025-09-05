import jpype
import jpype.imports

# Auto-generated wrapper for dqs
class dqsWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dqs(*args, **kwargs)

    a = dqs.a
    def dqs(self, ):
        return self.obj.dqs()

    def a(self, ):
        return dqs.a()

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def IllegalStateException(self, feature, biome"):
        return self.obj.IllegalStateException(feature, biome")

    def b(self, ):
        return self.obj.b()
