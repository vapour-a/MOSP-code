import jpype
import jpype.imports

# Auto-generated wrapper for anx
class anxWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = anx(*args, **kwargs)

    def a(self, $$0, $$1, $$2):
        return anx.a($$0, $$1, $$2)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0, $$1):
        return anx.a($$0, $$1)
