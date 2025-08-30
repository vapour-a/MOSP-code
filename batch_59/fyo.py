import jpype
import jpype.imports

# Auto-generated wrapper for fyo
class fyoWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fyo(*args, **kwargs)

    def fyo(self, $$0, $$1, $$2):
        return self.obj.fyo($$0, $$1, $$2)

    def b(self, $$0):
        return self.obj.b($$0)

    def qr(self, ):
        return self.obj.qr()

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def b(self, ):
        return self.obj.b()

    def r(self, ):
        return self.obj.r()
