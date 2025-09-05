import jpype
import jpype.imports

# Auto-generated wrapper for eos
class eosWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eos(*args, **kwargs)

    def a(self, $$0):
        return eos.a($$0)

    def eos(self, ):
        return self.obj.eos()

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
