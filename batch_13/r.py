import jpype
import jpype.imports

# Auto-generated wrapper for r
class rWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = r(*args, **kwargs)

    def r(self, $$0):
        return self.obj.r($$0)

    def uncaughtException(self, $$0, $$1):
        return self.obj.uncaughtException($$0, $$1)
