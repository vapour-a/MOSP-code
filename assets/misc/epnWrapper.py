import jpype
import jpype.imports

# Auto-generated wrapper for epn
class epnWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = epn(*args, **kwargs)

    def a(self, $$0):
        return epn.a($$0)

    def a(self, $$0, $$1, $$2):
        return epn.a($$0, $$1, $$2)

    def end(self, ):
        return self.obj.end()
