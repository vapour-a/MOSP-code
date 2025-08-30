import jpype
import jpype.imports

# Auto-generated wrapper for cyt
class cytWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cyt(*args, **kwargs)

    def cyt(self, $$0):
        return self.obj.cyt($$0)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def eei(self, 0.25D, 0.05000000074505806D, 0.25D):
        return self.obj.eei(0.25D, 0.05000000074505806D, 0.25D)
