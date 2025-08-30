import jpype
import jpype.imports

# Auto-generated wrapper for eva
class evaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eva(*args, **kwargs)

    def C(self, ):
        return self.obj.C()
