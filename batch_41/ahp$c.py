import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def onLevelChange(self, paramclt, paramIntSupplier, paramInt, paramIntConsumer):
        return self.obj.onLevelChange(paramclt, paramIntSupplier, paramInt, paramIntConsumer)
