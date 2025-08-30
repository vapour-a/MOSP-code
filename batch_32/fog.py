import jpype
import jpype.imports

# Auto-generated wrapper for fog
class fogWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fog(*args, **kwargs)

    def acq(self, "textures/entity/spider/cave_spider.png"):
        return self.obj.acq("textures/entity/spider/cave_spider.png")

    def fog(self, $$0):
        return self.obj.fog($$0)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def a(self, $$0):
        return self.obj.a($$0)
