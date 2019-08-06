from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
x, y, z = mc.player.getPos()
print("Orange: 1, Magenta: 2, Light Blue: 3, Yellow: 4, Lime: 5, Pink: 6, Gray: 7, Light Gray: 8, Cyan: 9, Purple: 10, Blue: 11, Brown: 12, Dark Green, 13, Red: 14, Black: 15")
color = input("What color should the structure be?")
g = int(color)
color_2 = input("What color should the structure be?")
h = int(color_2)
print("Dandelion: 37, Blue Orchid: 38, 2, Mini Oak Tree: 6, Mini Birch Sapling: 6, 2")
plant = input("What plant would you like for your house? (If Orchid or Birch type first number here and second next.")
j = int(plant)
plant_2 = input("Type second number here. If non-applicable type 0.")
k = int(plant_2)
plant_left = input("What plant would you like on the left of your bookshelf?")
l = int(plant_left)
plant_left_2 = input("Type second number here.")
m = int(plant_left_2)
plant_right = input("What plant would you like on the right of your bookshelf?")
n = int(plant_right)
plant_right_2 = input("Type second number here.")
o = int(plant_right_2)
wool = 35
air = 0
glass = 20
sign = 63
gate = 107
dandelion = 37
oak_sapling = 6
birch_sapling = 6, 2
blue_orchid = 38, 1
mc.setBlocks(x+1, y, z+1, x+7, y+3, z+7, 35, g)
mc.setBlocks(x+1, y-1, z+1, x+7, y-1, z+7, 35, h)
mc.setBlocks(x+2, y, z+2, x+6, y+2, z+6, 0)
mc.setBlocks(x+1, y+1, z+2, x+1, y+2, z+6, 102)
mc.setBlocks(x+4, y+1, z+1, x+6, y+2, z+1, 102)
mc.setBlocks(x+2, y+1, z+7, x+6, y+2, z+7, 102)

mc.setBlocks(x+3, y-1, z+5, x+3, y-1, z+5, 61)
mc.setBlocks(x+3, y, z+6, x+3, y, z+6, 54)
mc.setBlocks(x+2, y-1, z+5, x+2, y-1, z+5, 58)
mc.setBlocks(x+2, y, z+6, x+2, y, z+6, 2)
mc.setBlocks(x+2, y+1, z+6, x+2, y+1, z+6, j, k)

mc.setBlocks(x+6, y, z+2, x+6, y, z+2, 2)
mc.setBlocks(x+6, y, z+6, x+6, y, z+6, 2)
mc.setBlocks(x+6, y, z+3, x+6, y+2, z+5, 47)
mc.setBlocks(x+6, y+1, z+2, x+6, y+1, z+2, l, m)
mc.setBlocks(x+6, y+1, z+6, x+6, y+1, z+6, n, o)

mc.setBlocks(x+2, y+3, z+2, x+2, y+3, z+2, 89)
mc.setBlocks(x+2, y+3, z+6, x+2, y+3, z+6, 89)
mc.setBlocks(x+5, y-1, z+4, x+5, y-1, z+4, 89)
mc.setBlocks(x+6, y+2, z+2, x+6, y+2, z+2, 50)
mc.setBlocks(x+6, y+2, z+6, x+6, y+2, z+6, 50)


mc.setBlocks(x+2, y, z+1, x+2, y, z+1, 107)
mc.setBlocks(x+2, y+1, z+1, x+2, y+1, z+1, 0)
#mc.setBlocks(x+2, y, z+1, x+2, y+1, z+1, 63)