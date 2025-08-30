import jpype
import jpype.imports

# Auto-generated wrapper for fhp
class fhpWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fhp(*args, **kwargs)

    def createParticle(self, paramT, paramfew, paramDouble1, paramDouble2, paramDouble3, paramDouble4, paramDouble5, paramDouble6):
        return self.obj.createParticle(paramT, paramfew, paramDouble1, paramDouble2, paramDouble3, paramDouble4, paramDouble5, paramDouble6)

    def createParticle(self, param1T, param1few, param1Double1, param1Double2, param1Double3, param1Double4, param1Double5, param1Double6):
        return self.obj.createParticle(param1T, param1few, param1Double1, param1Double2, param1Double3, param1Double4, param1Double5, param1Double6)
