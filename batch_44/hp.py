import jpype
import jpype.imports

# Auto-generated wrapper for hp
class hpWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = hp(*args, **kwargs)

    def hp(self, $$0, $$1, $$2):
        return self.obj.hp($$0, $$1, $$2)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def c(self, ):
        return self.obj.c()
