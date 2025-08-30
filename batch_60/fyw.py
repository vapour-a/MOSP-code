import jpype
import jpype.imports

# Auto-generated wrapper for fyw
class fywWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fyw(*args, **kwargs)

    def create(self, param1InputStream):
        return self.obj.create(param1InputStream)

    def close(self, ):
        return self.obj.close()

    def fyw(self, $$0, $$1):
        return self.obj.fyw($$0, $$1)

    def BufferedInputStream(self, $$1):
        return self.obj.BufferedInputStream($$1)

    def b(self, this.c):
        return self.obj.b(this.c)

    def a(self, ):
        return self.obj.a()

    def a(self, $$0):
        return self.obj.a($$0)

    def b(self, this.c):
        return self.obj.b(this.c)

    def close(self, ):
        return self.obj.close()
