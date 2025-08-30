import jpype
import jpype.imports

# Auto-generated wrapper for fve
class fveWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fve(*args, **kwargs)

    def fve(self, $$0, $$1, $$2):
        return self.obj.fve($$0, $$1, $$2)

    def AtomicInteger(self, $$2):
        return self.obj.AtomicInteger($$2)

    def a(self, ):
        return self.obj.a()

    def IOException(self, this.a, $$2):
        return self.obj.IOException(this.a, $$2)

    def b(self, ):
        return self.obj.b()
