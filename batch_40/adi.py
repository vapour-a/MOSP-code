import jpype
import jpype.imports

# Auto-generated wrapper for adi
class adiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = adi(*args, **kwargs)

    def adi(self, $$0, $$1):
        return self.obj.adi($$0, $$1)

    def a(self, ):
        return self.obj.a()

    def run(self, ):
        return self.obj.run()
