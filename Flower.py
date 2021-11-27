from mcpi.minecraft import Minecraft
import random
mc=Minecraft.create("anorfire.club")
blocktype=0
uuid=mc.getPlayerEntityId("ambi1221")
while 1:
    blocktype=random.randint(1,8)
    x,y,z=mc.entity.getTilePos(uuid)             
    mc.setBlocks(x,y,z+5,y,z+5,38,blocktype
