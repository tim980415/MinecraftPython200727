# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:49:57 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

while True:
    mc.postToChat("你的位置-X:"+str(x)+" Y:"+str(y)+"Z:"+str(z))
    time.sleep(2)