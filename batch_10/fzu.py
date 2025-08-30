import jpype
import jpype.imports

# Auto-generated wrapper for fzu
class fzuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fzu(*args, **kwargs)

    def fzu(self, $$0, $$1):
        return self.obj.fzu($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)
