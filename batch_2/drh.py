import jpype
import jpype.imports

# Auto-generated wrapper for drh
class drhWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = drh(*args, **kwargs)

    def a_(self, paramdrf, paramapf, paramgu):
        return self.obj.a_(paramdrf, paramapf, paramgu)

    def b(self, ):
        return self.obj.b()
