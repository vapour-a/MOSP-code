import jpype
import jpype.imports

# Auto-generated wrapper for eug
class eugWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eug(*args, **kwargs)

    def a(self, $$0, $$1, $$2):
        return eug.a($$0, $$1, $$2)

    def eug(self, $$1, $$2, (enq<?>[]):
        return self.obj.eug($$1, $$2, (enq<?>[])

    def eug(self, $$0, $$1, $$2, $$3):
        return self.obj.eug($$0, $$1, $$2, $$3)

    def b(self, ):
        return self.obj.b()
