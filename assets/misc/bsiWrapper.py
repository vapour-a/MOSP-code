import jpype
import jpype.imports

# Auto-generated wrapper for bsi
class bsiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bsi(*args, **kwargs)

    def bsi(self, $$0, $$1):
        return self.obj.bsi($$0, $$1)

    def b(self, $$0):
        return self.obj.b($$0)

    def qr(self, ):
        return self.obj.qr()

    def l(self, ):
        return self.obj.l()

    def gh(self, ):
        return self.obj.gh()
