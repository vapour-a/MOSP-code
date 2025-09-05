import jpype
import jpype.imports

# Auto-generated wrapper for bpu
class bpuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bpu(*args, **kwargs)

    def a(self, ):
        return self.obj.a()

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
