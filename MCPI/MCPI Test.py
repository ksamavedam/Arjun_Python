from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
x, y, z = mc.player.getPos()
mc.setBlocks(x+1, y, z+1, x, y, z, 355)