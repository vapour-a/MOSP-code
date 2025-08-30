import jpype
import jpype.imports

# Auto-generated wrapper for j
class jWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = j(*args, **kwargs)

    def c(self, ):
        return self.obj.c()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
