import jpype
import jpype.imports

# Auto-generated wrapper for cfi
class cfiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cfi(*args, **kwargs)

    def cfi(self, $$0, $$1):
        return self.obj.cfi($$0, $$1)

    def c(self, $$0):
        return self.obj.c($$0)
