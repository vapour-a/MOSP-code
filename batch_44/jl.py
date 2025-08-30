import jpype
import jpype.imports

# Auto-generated wrapper for jl
class jlWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = jl(*args, **kwargs)

    def jl(self, $$0, $$1, $$2):
        return self.obj.jl($$0, $$1, $$2)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, ):
        return self.obj.a()
