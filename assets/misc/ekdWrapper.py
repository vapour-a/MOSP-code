import jpype
import jpype.imports

# Auto-generated wrapper for ekd
class ekdWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ekd(*args, **kwargs)

    def a(self, $$0):
        return ekd.a($$0)

    def ekd(self, ):
        return self.obj.ekd()

    def JsonParser(self, ):
        return self.obj.JsonParser()

    def b(self, $$0):
        return ekd.b($$0)
