import jpype
import jpype.imports

# Auto-generated wrapper for mq
class mqWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = mq(*args, **kwargs)

    def mq(self, $$0, $$1):
        return self.obj.mq($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)
