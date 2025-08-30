import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def GameProfile(self, $$0, null):
        return self.obj.GameProfile($$0, null)

    def a(self, ):
        return self.obj.a()
