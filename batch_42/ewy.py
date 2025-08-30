import jpype
import jpype.imports

# Auto-generated wrapper for ewy
class ewyWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ewy(*args, **kwargs)

    def Vector3f(self, 0.9765628F, 0.9765628F, 0.9765628F):
        return self.obj.Vector3f(0.9765628F, 0.9765628F, 0.9765628F)

    def ewy(self, $$0, $$1, $$2):
        return self.obj.ewy($$0, $$1, $$2)

    def b(self, ):
        return self.obj.b()

    def b(self, $$0, $$1):
        return self.obj.b($$0, $$1)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def l(self, ):
        return self.obj.l()
