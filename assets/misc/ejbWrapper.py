import jpype
import jpype.imports

# Auto-generated wrapper for ejb
class ejbWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ejb(*args, **kwargs)

    def ejb(self, $$0, $$1):
        return self.obj.ejb($$0, $$1)

    def a(self, $$0):
        return ejb.a($$0)

    def ejb(self, $$2, $$3):
        return self.obj.ejb($$2, $$3)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()
