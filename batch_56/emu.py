import jpype
import jpype.imports

# Auto-generated wrapper for emu
class emuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = emu(*args, **kwargs)

    def emu(self, $$0, $$1, $$2):
        return self.obj.emu($$0, $$1, $$2)

    def run(self, ):
        return self.obj.run()
