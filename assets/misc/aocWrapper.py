import jpype
import jpype.imports

# Auto-generated wrapper for aoc
class aocWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = aoc(*args, **kwargs)

    def a(self, $$0, $$1):
        return aoc.a($$0, $$1)

    def fetch(self, param1Int1, param1Int2, param1Int3):
        return self.obj.fetch(param1Int1, param1Int2, param1Int3)
