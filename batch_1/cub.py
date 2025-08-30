import jpype
import jpype.imports

# Auto-generated wrapper for cub
class cubWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cub(*args, **kwargs)

    def a(self, paramcls, paramgu, paramdcb, paramdxd):
        return self.obj.a(paramcls, paramgu, paramdcb, paramdxd)

    def a(self, paramcmn, paramgu, paramdcb, paramdxe):
        return self.obj.a(paramcmn, paramgu, paramdcb, paramdxe)
