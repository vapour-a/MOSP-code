import jpype
import jpype.imports

# Auto-generated wrapper for cpt
class cptWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cpt(*args, **kwargs)

    def c(self, paramcmn, paramgu, paramdcb):
        return self.obj.c(paramcmn, paramgu, paramdcb)

    def am_(self, ):
        return self.obj.am_()
