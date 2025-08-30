import jpype
import jpype.imports

# Auto-generated wrapper for ekk
class ekkWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ekk(*args, **kwargs)

    def ekk(self, $$0):
        return self.obj.ekk($$0)

    def uncaughtException(self, $$0, $$1):
        return self.obj.uncaughtException($$0, $$1)
