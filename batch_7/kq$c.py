import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def create(self, paramcpn, paramacq, paramlh, BiConsumer<acq, paramBiConsumer):
        return self.obj.create(paramcpn, paramacq, paramlh, BiConsumer<acq, paramBiConsumer)
