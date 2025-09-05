import jpype
import jpype.imports

# Auto-generated wrapper for cyx
class cyxWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cyx(*args, **kwargs)

    def cyx(self, $$0):
        return self.obj.cyx($$0)

    def b(self, $$0, $$1, $$2, $$3, $$4):
        return self.obj.b($$0, $$1, $$2, $$3, $$4)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)
