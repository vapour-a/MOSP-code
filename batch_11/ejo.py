import jpype
import jpype.imports

# Auto-generated wrapper for ejo
class ejoWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ejo(*args, **kwargs)

    def a(self, $$0):
        return ejo.a($$0)

    def ejo(self, ):
        return self.obj.ejo()

    def JsonParser(self, ):
        return self.obj.JsonParser()
