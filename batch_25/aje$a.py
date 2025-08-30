import jpype
import jpype.imports

# Auto-generated wrapper for a
class aWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = a(*args, **kwargs)

    def ignoreOverThreshold(self, $$0):
        return a.ignoreOverThreshold($$0)

    def select(self, $$0):
        return a.select($$0)

    def shouldIgnore(self, paramString, paramInt):
        return self.obj.shouldIgnore(paramString, paramInt)
