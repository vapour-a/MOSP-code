import jpype
import jpype.imports

# Auto-generated wrapper for ecd
class ecdWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ecd(*args, **kwargs)

    def b(self, parama):
        return self.obj.b(parama)

    def a_(self, $$0, Function<E, $$1):
        return self.obj.a_($$0, Function<E, $$1)

    def d(self, ):
        return self.obj.d()
