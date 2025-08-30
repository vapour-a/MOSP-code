import jpype
import jpype.imports

# Auto-generated wrapper for dru
class druWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dru(*args, **kwargs)

    def a(self, $$0):
        return dru.a($$0)

    def acq(self, $$0):
        return self.obj.acq($$0)
