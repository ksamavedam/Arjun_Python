from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
x, y, z = mc.player.getPos()
#height = input("How tall should the structure be?")
#a = int(height)
#width = input("How wide should the structure be?")
#b = int(width)
#length = input("How long should the structure be?")
#c = int(length)
print("Orange: 1, Magenta: 2, Light Blue: 3, Yellow: 4, Lime: 5, Pink: 6, Gray: 7, Light Gray: 8, Cyan: 9, Purple: 10, Blue: 11, Brown: 12, Dark Green, 13, Red: 14, Black: 15")
color = input("What color should the structure be?")
g = int(color)
wool = 35
air = 0
glass = 20
sign = 63
gate = 107
mc.setBlocks(x+1, y, z+1, x+3, y+2, z+3, 35, g)
mc.setBlocks(x+2, y, z+2, x+2, y+1, z+2, 0)
mc.setBlocks(x+1, y+1, z+2, x+1, y+1, z+2, 20)
mc.setBlocks(x+2, y, z+1, x+2, y, z+1, 107)
mc.setBlocks(x+2, y+1, z+1, x+2, y+1, z+1, 0)
