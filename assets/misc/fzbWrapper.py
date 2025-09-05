import jpype
import jpype.imports

# Auto-generated wrapper for fzb
class fzbWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fzb(*args, **kwargs)

    def a(self, paramfxy, paramfzd):
        return self.obj.a(paramfxy, paramfzd)
