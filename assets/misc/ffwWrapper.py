import jpype
import jpype.imports

# Auto-generated wrapper for ffw
class ffwWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ffw(*args, **kwargs)

    def predict(self, paramInt):
        return self.obj.predict(paramInt)
