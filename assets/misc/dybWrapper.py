import jpype
import jpype.imports

# Auto-generated wrapper for dyb
class dybWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dyb(*args, **kwargs)

    def dyb(self, $$0, $$1, $$2, $$3):
        return self.obj.dyb($$0, $$1, $$2, $$3)
