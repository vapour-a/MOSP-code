import jpype
import jpype.imports

# Auto-generated wrapper for fbj
class fbjWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fbj(*args, **kwargs)

    def fbj(self, $$0):
        return self.obj.fbj($$0)

    def a(self, $$0):
        return fbj.a($$0)

    def b(self, ):
        return fbj.b()

    def fem(self, ):
        return self.obj.fem()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, ):
        return self.obj.a()
