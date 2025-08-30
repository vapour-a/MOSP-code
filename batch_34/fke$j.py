import jpype
import jpype.imports

# Auto-generated wrapper for j
class jWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = j(*args, **kwargs)

    def j(self, $$0, $$1):
        return self.obj.j($$0, $$1)

    def Matrix4f(self, ):
        return self.obj.Matrix4f()
