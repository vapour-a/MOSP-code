import jpype
import jpype.imports

# Auto-generated wrapper for drm
class drmWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = drm(*args, **kwargs)

    def drm(self, $$0, $$1, $$2):
        return self.obj.drm($$0, $$1, $$2)

    def a(self, $$0, $$1, $$2):
        return drm.a($$0, $$1, $$2)

    def drm(self, $$0, $$1, $$2):
        return self.obj.drm($$0, $$1, $$2)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def b(self, ):
        return self.obj.b()
