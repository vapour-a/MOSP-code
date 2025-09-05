import jpype
import jpype.imports

# Auto-generated wrapper for dsj
class dsjWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dsj(*args, **kwargs)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def codec(self, ):
        return self.obj.codec()
