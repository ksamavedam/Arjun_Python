from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
x, y, z = mc.player.getPos()
length = input("How long should one side of the base layer be?")
a = int(length)

mc.setBlocks(x+1, y, z+1, x+a, y, z+a, 24)
mc.setBlocks(x+1, y+1, z+1, x+a-2, y+1, z+a-2, 24)