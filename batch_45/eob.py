import jpype
import jpype.imports

# Auto-generated wrapper for eob
class eobWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eob(*args, **kwargs)

    def eob(self, $$0, $$1, $$2, $$3):
        return self.obj.eob($$0, $$1, $$2, $$3)

    def a(self, $$0):
        return self.obj.a($$0)

    def n(self, ):
        return self.obj.n()
