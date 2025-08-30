import jpype
import jpype.imports

# Auto-generated wrapper for null
class nullWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = null(*args, **kwargs)

    def onProfileLookupSucceeded(self, $$0):
        return self.obj.onProfileLookupSucceeded($$0)

    def onProfileLookupFailed(self, $$0, $$1):
        return self.obj.onProfileLookupFailed($$0, $$1)
