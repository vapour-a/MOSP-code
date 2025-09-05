import jpype
import jpype.imports

# Auto-generated wrapper for crc
class crcWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = crc(*args, **kwargs)

    def crc(self, $$0, $$1):
        return self.obj.crc($$0, $$1)

    def b(self, $$0, $$1, $$2, $$3, $$4):
        return self.obj.b($$0, $$1, $$2, $$3, $$4)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
