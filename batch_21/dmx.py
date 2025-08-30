import jpype
import jpype.imports

# Auto-generated wrapper for dmx
class dmxWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dmx(*args, **kwargs)

    def a(self, $$0):
        return dmx.a($$0)

    def dmx(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6):
        return self.obj.dmx($$0, $$1, $$2, $$3, $$4, $$5, $$6)

    def ObjectArrayList(self, 6):
        return self.obj.ObjectArrayList(6)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)
