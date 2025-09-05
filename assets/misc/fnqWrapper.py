import jpype
import jpype.imports

# Auto-generated wrapper for fnq
class fnqWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fnq(*args, **kwargs)

    def a(self, ):
        return self.obj.a()

    def a(self, $$0):
        return self.obj.a($$0)

    def b(self, $$0):
        return self.obj.b($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4):
        return self.obj.a($$0, $$1, $$2, $$3, $$4)

    def a(self, $$0, $$1, $$2):
        return fnq.a($$0, $$1, $$2)
