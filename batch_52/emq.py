import jpype
import jpype.imports

# Auto-generated wrapper for emq
class emqWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = emq(*args, **kwargs)

    def emq(self, $$0, $$1, $$2, $$3):
        return self.obj.emq($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
