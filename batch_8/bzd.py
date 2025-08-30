import jpype
import jpype.imports

# Auto-generated wrapper for bzd
class bzdWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bzd(*args, **kwargs)

    def j(self, ):
        return self.obj.j()
