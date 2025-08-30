import jpype
import jpype.imports

# Auto-generated wrapper for bku
class bkuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bku(*args, **kwargs)

    def a(self, $$0):
        return bku.a($$0)

    def a(self, $$0, 10, 7):
        return self.obj.a($$0, 10, 7)

    def a(self, $$0, $$1, $$2):
        return bku.a($$0, $$1, $$2)
