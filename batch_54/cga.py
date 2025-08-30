import jpype
import jpype.imports

# Auto-generated wrapper for cga
class cgaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cga(*args, **kwargs)

    def a(self, $$0):
        return cga.a($$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, ):
        return cga.a()

    def ObjectLinkedOpenCustomHashSet(self, a):
        return self.obj.ObjectLinkedOpenCustomHashSet(a)
