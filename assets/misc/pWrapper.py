import jpype
import jpype.imports

# Auto-generated wrapper for p
class pWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = p(*args, **kwargs)

    def p(self, $$0, $$1, $$2):
        return self.obj.p($$0, $$1, $$2)

    def p(self, $$0):
        return self.obj.p($$0)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return p.a($$0, $$1, $$2, $$3, $$4, $$5)

    def p(self, $$4, $$6, $$5):
        return self.obj.p($$4, $$6, $$5)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6)
