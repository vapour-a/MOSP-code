import jpype
import jpype.imports

# Auto-generated wrapper for fcb
class fcbWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fcb(*args, **kwargs)

    def fcb(self, Function<acq, $$0):
        return self.obj.fcb(Function<acq, $$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, parameij, paramein, paramInt1, paramInt2, paramFloat1, paramFloat2, paramFloat3, paramFloat4):
        return self.obj.a(parameij, paramein, paramInt1, paramInt2, paramFloat1, paramFloat2, paramFloat3, paramFloat4)
