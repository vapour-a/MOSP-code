import jpype
import jpype.imports

# Auto-generated wrapper for dlg
class dlgWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dlg(*args, **kwargs)

    def dlg(self, $$0):
        return self.obj.dlg($$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return dlg.a($$0, $$1, $$2, $$3, $$4, $$5)

    def c(self, $$0):
        return dlg.c($$0)
