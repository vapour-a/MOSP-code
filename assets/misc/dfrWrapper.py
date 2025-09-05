import jpype
import jpype.imports

# Auto-generated wrapper for dfr
class dfrWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dfr(*args, **kwargs)

    def onChunkStatusChange(self, paramclt, paramahy):
        return self.obj.onChunkStatusChange(paramclt, paramahy)
