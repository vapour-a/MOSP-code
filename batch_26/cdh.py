import jpype
import jpype.imports

# Auto-generated wrapper for cdh
class cdhWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cdh(*args, **kwargs)

    def cdh(self, $$0):
        return self.obj.cdh($$0)

    def a(self, $$0, $$1, $$2):
        return cdh.a($$0, $$1, $$2)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def StringReader(self, $$6):
        return self.obj.StringReader($$6)
