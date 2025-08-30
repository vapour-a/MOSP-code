import jpype
import jpype.imports

# Auto-generated wrapper for dri
class driWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dri(*args, **kwargs)

    def codec(self, ):
        return self.obj.codec()

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
