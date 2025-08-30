import jpype
import jpype.imports

# Auto-generated wrapper for bma
class bmaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bma(*args, **kwargs)

    def bma(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.bma($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, ):
        return self.obj.a()

    def a(self, $$0):
        return bma.a($$0)
