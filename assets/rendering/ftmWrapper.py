import jpype
import jpype.imports

# Auto-generated wrapper for ftm
class ftmWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ftm(*args, **kwargs)

    def acq(self, "textures/entity/spider_eyes.png"):
        return self.obj.acq("textures/entity/spider_eyes.png")

    def ftm(self, fqt<T, $$0):
        return self.obj.ftm(fqt<T, $$0)

    def a(self, ):
        return self.obj.a()
