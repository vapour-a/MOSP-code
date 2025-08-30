import jpype
import jpype.imports

# Auto-generated wrapper for fzi
class fziWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fzi(*args, **kwargs)

    def fzi(self, $$0, $$1):
        return self.obj.fzi($$0, $$1)

    def a(self, ):
        return self.obj.a()

    def close(self, ):
        return self.obj.close()
