import jpype
import jpype.imports

# Auto-generated wrapper for dof
class dofWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dof(*args, **kwargs)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def dof(self, $$1):
        return self.obj.dof($$1)

    def dof(self, $$0):
        return self.obj.dof($$0)

    def a(self, ):
        return self.obj.a()
