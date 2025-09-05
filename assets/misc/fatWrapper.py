import jpype
import jpype.imports

# Auto-generated wrapper for fat
class fatWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fat(*args, **kwargs)

    def fat(self, $$0):
        return self.obj.fat($$0)

    def c(self, ):
        return fat.c()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
