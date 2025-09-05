import jpype
import jpype.imports

# Auto-generated wrapper for fur
class furWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fur(*args, **kwargs)

    def a(self, paramInt1, paramInt2):
        return self.obj.a(paramInt1, paramInt2)

    def close(self, ):
        return self.obj.close()
