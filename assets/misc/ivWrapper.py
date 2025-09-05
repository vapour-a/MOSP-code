import jpype
import jpype.imports

# Auto-generated wrapper for iv
class ivWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = iv(*args, **kwargs)

    def a(self, $$0, $$1):
        return iv.a($$0, $$1)

    def iy(self, $$1):
        return self.obj.iy($$1)

    def a(self, $$0, $$1, $$2, Function<iu<T>, $$3):
        return self.obj.a($$0, $$1, $$2, Function<iu<T>, $$3)

    def e(self, ):
        return self.obj.e()
