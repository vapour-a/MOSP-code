import jpype
import jpype.imports

# Auto-generated wrapper for ems
class emsWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ems(*args, **kwargs)

    def ems(self, $$0, $$1, $$2):
        return self.obj.ems($$0, $$1, $$2)

    def a(self, parameiz, paramLong):
        return self.obj.a(parameiz, paramLong)

    def run(self, ):
        return self.obj.run()
