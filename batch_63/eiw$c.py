import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def actionPerformed(self, $$0):
        return self.obj.actionPerformed($$0)

    def hash(self, {}, {}):
        return self.obj.hash({}, {})
