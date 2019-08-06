from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
#mc.postToChat("My name is  Awesomeguy99ab!")
x, y, z = mc.player.getPos()
mc.player.setPos(99, 100, 99)
#mc.setBlock(x+1, y, z, block.WOOL.id, 3)
#mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, block.WOOL.id, 3)