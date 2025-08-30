import jpype
import jpype.imports

# Auto-generated wrapper for csw
class cswWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = csw(*args, **kwargs)

    def csw(self, $$0):
        return self.obj.csw($$0)

    def d(self, $$0, $$1, $$2):
        return self.obj.d($$0, $$1, $$2)
