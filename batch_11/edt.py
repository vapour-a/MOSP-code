import jpype
import jpype.imports

# Auto-generated wrapper for edt
class edtWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = edt(*args, **kwargs)

    def handle(self, paramT, paramedv, paramLong):
        return self.obj.handle(paramT, paramedv, paramLong)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def a(self, param1qr, param1C):
        return self.obj.a(param1qr, param1C)

    def b(self, param1qr):
        return self.obj.b(param1qr)
