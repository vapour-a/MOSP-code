import jpype
import jpype.imports

# Auto-generated wrapper for fys
class fysWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fys(*args, **kwargs)

    def AtomicInteger(self, 0):
        return self.obj.AtomicInteger(0)

    def fys(self, $$0, $$1):
        return self.obj.fys($$0, $$1)

    def r(self, d):
        return self.obj.r(d)

    def DatagramSocket(self, ):
        return self.obj.DatagramSocket()

    def run(self, ):
        return self.obj.run()

    def DatagramPacket(self, $$1, $$1.length, $$2, 4445):
        return self.obj.DatagramPacket($$1, $$1.length, $$2, 4445)

    def interrupt(self, ):
        return self.obj.interrupt()

    def a(self, $$0, $$1):
        return fys.a($$0, $$1)

    def a(self, $$0):
        return fys.a($$0)

    def b(self, $$0):
        return fys.b($$0)
