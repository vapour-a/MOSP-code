import jpype
import jpype.imports

# Auto-generated wrapper for akn
class aknWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = akn(*args, **kwargs)

    def close(self, ):
        return self.obj.close()
