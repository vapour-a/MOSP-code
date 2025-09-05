import jpype
import jpype.imports

# Auto-generated wrapper for bev
class bevWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bev(*args, **kwargs)

    def bev(self, $$0, $$1, $$2):
        return self.obj.bev($$0, $$1, $$2)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
