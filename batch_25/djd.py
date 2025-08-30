import jpype
import jpype.imports

# Auto-generated wrapper for djd
class djdWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = djd(*args, **kwargs)

    a = djd.a
    def djd(self, ):
        return self.obj.djd()

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, ):
        return self.obj.a()
