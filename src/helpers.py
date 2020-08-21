#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def ips(c_time, c_speed):
    """ Computes items per second from a recipe and 
        assembler.
    
    c_time (float): Crafting time of recipe
    c_speed (float): Crafting speed of the assembler
    """
    return c_speed / c_time


def itf(ips, belt_speed):
    """ Computes number of assemblers needed to
        saturate the belt at belt_speed.
    
    ips (float): Items per second being created
    belt_speed (float): Throughput of belt
    """
    return belt_speed / ips


# Crafting times
T = {
    'iron_plate':    3.2,
    'copper_plate':  3.2,
    'steel_plate':   16
}

# Crafting speeds
S = {
    'player':            1,
    'stone_furnace':     1,
    'steel_furnace':     2,
    'electric_furnace':  2,
    'ass_1':            .5,
    'ass_2':            .75
}

# Belt speeds
B = {
    'yellow':  15,
    'red':     30,
    'blue':    45
}

