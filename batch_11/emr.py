import jpype
import jpype.imports

# Auto-generated wrapper for emr
class emrWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = emr(*args, **kwargs)

    def emr(self, $$0, $$1, $$2, $$3):
        return self.obj.emr($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
