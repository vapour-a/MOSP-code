import jpype
import jpype.imports

# Auto-generated wrapper for apt
class aptWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = apt(*args, **kwargs)

    def immediate(self, $$0):
        return apt.immediate($$0)

    def append(self, parama):
        return self.obj.append(parama)

    def submit(self, param1Executor):
        return self.obj.submit(param1Executor)
