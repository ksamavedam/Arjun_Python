from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
x, y, z = mc.player.getPos()
#mc.player.setPos(-99, 0, -160)
height = input("How tall should the structure be?")
a = int(height)
width = input("How wide should the structure be?")
b = int(width)
length = input("How long should the structure be?")
c = int(length)
print("Orange: 1, Magenta: 2, Light Blue: 3, Yellow: 4, Lime: 5, Pink: 6, Gray: 7, Light Gray: 8, Cyan: 9, Purple: 10, Blue: 11, Brown: 12, Dark Green, 13, Red: 14, Black: 15")
color = input("What color should the structure be?")
g = int(color)
wool = 35
air = 0
mc.setBlocks(x+1, y, z+1, x+c, y-1+a, z+b, 64)
