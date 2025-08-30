import jpype
import jpype.imports

# Auto-generated wrapper for csb
class csbWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = csb(*args, **kwargs)

    def a(self, paramgu, paramdcb):
        return self.obj.a(paramgu, paramdcb)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
