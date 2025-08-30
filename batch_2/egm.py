import jpype
import jpype.imports

# Auto-generated wrapper for egm
class egmWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = egm(*args, **kwargs)

    def close(self, ):
        return self.obj.close()

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, ):
        return self.obj.a()
