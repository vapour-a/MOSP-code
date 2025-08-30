import jpype
import jpype.imports

# Auto-generated wrapper for cns
class cnsWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cns(*args, **kwargs)

    def cns(self, $$0, $$1):
        return self.obj.cns($$0, $$1)

    def b(self, ):
        return self.obj.b()

    def a(self, ):
        return self.obj.a()

    def getNoiseBiome(self, $$0, $$1, $$2, $$3):
        return self.obj.getNoiseBiome($$0, $$1, $$2, $$3)
