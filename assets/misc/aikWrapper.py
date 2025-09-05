import jpype
import jpype.imports

# Auto-generated wrapper for aik
class aikWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = aik(*args, **kwargs)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def aik(self, $$0, $$1, $$2):
        return self.obj.aik($$0, $$1, $$2)

    def toString(self, ):
        return self.obj.toString()

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()
