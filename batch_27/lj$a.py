import jpype
import jpype.imports

# Auto-generated wrapper for a
class aWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = a(*args, **kwargs)

    def get(self, paramcpn):
        return self.obj.get(paramcpn)

    def create(self, $$0, BiConsumer<acq, $$1):
        return self.obj.create($$0, BiConsumer<acq, $$1)

    def get(self, $$0):
        return self.obj.get($$0)

    def createWithSuffix(self, $$0, $$1, BiConsumer<acq, $$2):
        return self.obj.createWithSuffix($$0, $$1, BiConsumer<acq, $$2)

    def get(self, $$0):
        return self.obj.get($$0)

    def updateTexture(self, $$0):
        return self.obj.updateTexture($$0)

    def get(self, $$1):
        return self.obj.get($$1)
