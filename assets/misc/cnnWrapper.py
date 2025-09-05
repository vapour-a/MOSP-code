import jpype
import jpype.imports

# Auto-generated wrapper for cnn
class cnnWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cnn(*args, **kwargs)

    def getNoiseBiome(self, paramInt1, paramInt2, paramInt3, paramf):
        return self.obj.getNoiseBiome(paramInt1, paramInt2, paramInt3, paramf)
