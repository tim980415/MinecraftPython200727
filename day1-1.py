# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:20:49 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

print(mc.player.getTilePos())