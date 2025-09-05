import jpype
import jpype.imports

# Auto-generated wrapper for ld
class ldWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ld(*args, **kwargs)

    def ld(self, $$0):
        return self.obj.ld($$0)

    def a(self, ):
        return self.obj.a()

    def JsonObject(self, ):
        return self.obj.JsonObject()
