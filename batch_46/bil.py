import jpype
import jpype.imports

# Auto-generated wrapper for bil
class bilWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bil(*args, **kwargs)

    def a(self, $$0, $$1, $$2):
        return bil.a($$0, $$1, $$2)

    def a(self, true, $$0, $$1, $$2):
        return self.obj.a(true, $$0, $$1, $$2)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)
