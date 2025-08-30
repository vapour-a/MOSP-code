import jpype
import jpype.imports

# Auto-generated wrapper for jr
class jrWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = jr(*args, **kwargs)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def acq(self, "textures/gui/advancements/backgrounds/nether.png"):
        return self.obj.acq("textures/gui/advancements/backgrounds/nether.png")

    def acq(self, "minecraft:chests/bastion_other"):
        return self.obj.acq("minecraft:chests/bastion_other")

    def acq(self, "minecraft:chests/bastion_treasure"):
        return self.obj.acq("minecraft:chests/bastion_treasure")

    def acq(self, "minecraft:chests/bastion_hoglin_stable"):
        return self.obj.acq("minecraft:chests/bastion_hoglin_stable")

    def acq(self, "minecraft:chests/bastion_bridge"):
        return self.obj.acq("minecraft:chests/bastion_bridge")
