import jpype
import jpype.imports

# Auto-generated wrapper for enj
class enjWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = enj(*args, **kwargs)

    def enj(self, $$0, $$1):
        return self.obj.enj($$0, $$1)

    def File(self, $$0, "hotbar.nbt"):
        return self.obj.File($$0, "hotbar.nbt")

    def fja(self, ):
        return self.obj.fja()

    def b(self, ):
        return self.obj.b()

    def a(self, ):
        return self.obj.a()

    def qr(self, ):
        return self.obj.qr()

    def a(self, $$0):
        return self.obj.a($$0)
