import jpype
import jpype.imports

# Auto-generated wrapper for fiw
class fiwWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fiw(*args, **kwargs)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, ):
        return self.obj.a()

    def eeh(self, this.a, this.b):
        return self.obj.eeh(this.a, this.b)

    def b(self, ):
        return self.obj.b()
