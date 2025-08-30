import jpype
import jpype.imports

# Auto-generated wrapper for fwo
class fwoWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fwo(*args, **kwargs)

    def b(self, $$0):
        return self.obj.b($$0)

    def fwn(self, $$1, $$2):
        return self.obj.fwn($$1, $$2)

    def a(self, ):
        return self.obj.a()
