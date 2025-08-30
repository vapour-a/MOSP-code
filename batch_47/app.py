import jpype
import jpype.imports

# Auto-generated wrapper for app
class appWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = app(*args, **kwargs)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7)

    def canSpawnOn(self, param1aif, param1gu1, param1dcb1, param1gu2, param1dcb2):
        return self.obj.canSpawnOn(param1aif, param1gu1, param1dcb1, param1gu2, param1dcb2)

    def a(self, $$0, $$1, $$2, $$3):
        return app.a($$0, $$1, $$2, $$3)
