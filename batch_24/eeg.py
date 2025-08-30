import jpype
import jpype.imports

# Auto-generated wrapper for eeg
class eegWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eeg(*args, **kwargs)

    def eeg(self, $$0):
        return self.obj.eeg($$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def c(self, ):
        return self.obj.c()

    def e(self, ):
        return self.obj.e()
