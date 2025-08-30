import jpype
import jpype.imports

# Auto-generated wrapper for sh
class shWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = sh(*args, **kwargs)

    def sh(self, $$0):
        return self.obj.sh($$0)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def EncoderException(self, $$1):
        return self.obj.EncoderException($$1)
