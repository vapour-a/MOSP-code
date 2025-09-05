import jpype
import jpype.imports

# Auto-generated wrapper for fzj
class fzjWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fzj(*args, **kwargs)

    def log(self, paramfzh):
        return self.obj.log(paramfzh)
