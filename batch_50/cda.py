import jpype
import jpype.imports

# Auto-generated wrapper for cda
class cdaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cda(*args, **kwargs)

    def a(self, parambys):
        return self.obj.a(parambys)
