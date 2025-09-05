import jpype
import jpype.imports

# Auto-generated wrapper for dte
class dteWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dte(*args, **kwargs)

    def dte(self, Either<acq, $$0, $$1, $$2):
        return self.obj.dte(Either<acq, $$0, $$1, $$2)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def a(self, ):
        return self.obj.a()

    def toString(self, ):
        return self.obj.toString()
