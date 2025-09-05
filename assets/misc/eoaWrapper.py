import jpype
import jpype.imports

# Auto-generated wrapper for eoa
class eoaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eoa(*args, **kwargs)

    def eoa(self, $$0, $$1):
        return self.obj.eoa($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)
