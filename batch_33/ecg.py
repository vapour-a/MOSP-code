import jpype
import jpype.imports

# Auto-generated wrapper for ecg
class ecgWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ecg(*args, **kwargs)

    def ecg(self, ):
        return self.obj.ecg()

    def b(self, ):
        return self.obj.b()

    def a(self, ):
        return self.obj.a()

    def a(self, $$0):
        return self.obj.a($$0)

    def c(self, ):
        return self.obj.c()

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def b(self, $$0, $$1):
        return self.obj.b($$0, $$1)
