import jpype
import jpype.imports

# Auto-generated wrapper for cse
class cseWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cse(*args, **kwargs)

    def a(self, $$0, $$1, $$2, $$3, $$4):
        return self.obj.a($$0, $$1, $$2, $$3, $$4)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def a(self, $$0):
        return self.obj.a($$0)
