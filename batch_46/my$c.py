import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def empty(self, ):
        return self.obj.empty()

    def contains(self, $$0):
        return self.obj.contains($$0)

    def apply(self, $$0):
        return self.obj.apply($$0)
