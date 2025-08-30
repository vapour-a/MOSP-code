import jpype
import jpype.imports

# Auto-generated wrapper for dwc
class dwcWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dwc(*args, **kwargs)

    def codec(self, ):
        return self.obj.codec()

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
