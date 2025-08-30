import jpype
import jpype.imports

# Auto-generated wrapper for elb
class elbWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = elb(*args, **kwargs)

    def elb(self, $$0, $$1, $$2):
        return self.obj.elb($$0, $$1, $$2)

    def b(self, ):
        return self.obj.b()

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)
