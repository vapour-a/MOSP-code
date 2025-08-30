import jpype
import jpype.imports

# Auto-generated wrapper for eev
class eevWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eev(*args, **kwargs)

    def eev(self, $$0, $$1, $$2, $$3):
        return self.obj.eev($$0, $$1, $$2, $$3)

    def a(self, $$0):
        return self.obj.a($$0)

    def size(self, ):
        return self.obj.size()

    def a(self, ):
        return self.obj.a()
