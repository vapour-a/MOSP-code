import jpype
import jpype.imports

# Auto-generated wrapper for adl
class adlWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = adl(*args, **kwargs)

    def a(self, $$0, $$1):
        return adl.a($$0, $$1)

    def a(self, $$0):
        return adl.a($$0)

    def a(self, $$0, $$1, $$2, $$3):
        return adl.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1, $$2):
        return adl.a($$0, $$1, $$2)

    def ObjectArrayList(self, ):
        return self.obj.ObjectArrayList()

    def accept(self, param1ae, param1Boolean):
        return self.obj.accept(param1ae, param1Boolean)
