import jpype
import jpype.imports

# Auto-generated wrapper for bia
class biaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bia(*args, **kwargs)

    def a(self, $$0, BiPredicate<E, $$1):
        return self.obj.a($$0, BiPredicate<E, $$1)

    def a(self, $$0, $$1, $$2):
        return bia.a($$0, $$1, $$2)
