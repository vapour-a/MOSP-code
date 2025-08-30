import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def SecureRandom(self, ):
        return self.obj.SecureRandom()

    def a(self, ):
        return c.a()
