import jpype
import jpype.imports

# Auto-generated wrapper for dht
class dhtWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dht(*args, **kwargs)

    def a(self, $$0):
        return self.obj.a($$0)

    def acq(self, $$0):
        return self.obj.acq($$0)

    def a(self, $$0, $$1, $$2):
        return dht.a($$0, $$1, $$2)
