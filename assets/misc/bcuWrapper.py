import jpype
import jpype.imports

# Auto-generated wrapper for bcu
class bcuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bcu(*args, **kwargs)

    def bcu(self, $$0, $$1):
        return self.obj.bcu($$0, $$1)

    def a(self, $$0, $$1):
        return bcu.a($$0, $$1)

    def bcu(self, $$0, $$1):
        return self.obj.bcu($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def c(self, ):
        return self.obj.c()

    def toString(self, ):
        return self.obj.toString()
