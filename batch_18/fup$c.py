import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def ehk(self, $$1, $$2, false):
        return self.obj.ehk($$1, $$2, false)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def a(self, $$0, $$1, $$2, $$3, $$4):
        return self.obj.a($$0, $$1, $$2, $$3, $$4)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def close(self, ):
        return self.obj.close()
