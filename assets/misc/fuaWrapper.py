import jpype
import jpype.imports

# Auto-generated wrapper for fua
class fuaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fua(*args, **kwargs)

    def call(self, $$0, $$1, $$2, $$3):
        return self.obj.call($$0, $$1, $$2, $$3)

    def unclampedCall(self, paramcfz, paramfew, parambfz, paramInt):
        return self.obj.unclampedCall(paramcfz, paramfew, parambfz, paramInt)
