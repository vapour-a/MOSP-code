import jpype
import jpype.imports

# Auto-generated wrapper for j
class jWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = j(*args, **kwargs)

    def j(self, parambrv, $$0, $$1, $$2):
        return self.obj.j(parambrv, $$0, $$1, $$2)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()
