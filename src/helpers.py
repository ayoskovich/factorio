#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ips(c_time, c_speed):
    """ Computes items per second from a recipe and 
        assembler.
    
    c_time (float): Crafting time of recipe
    c_speed (float): Crafting speed of the assembler
    """
    return c_speed / c_time


def itf(c_time, c_speed, belt_speed):
    """ Computes number of assemblers needed to
        saturate the belt at belt_speed.
    
    ips (float): Items per second being created
    belt_speed (float): Throughput of belt
    """
    return belt_speed / ips(c_time, c_speed)


# Crafting times
CT = {
    'iron_plate':    3.2,
    'iron_gear':      .5,
    'pipe':           .5,
    'copper_plate':  3.2,
    'steel_plate':   16
}


# Crafting speeds
CS = {
    'player':             1,
    'stone_furnace':      1,
    'steel_furnace':      2,
    'electric_furnace':   2,
    'ass_1':             .5,
    'ass_2':             .75
}


# Belt speeds
BS = {
    'yellow':  {
        'throughput':15, # Items per game second for 2 lanes
        'speed':1.875,   # Tiles per game second
        'density':8      # Items per tile
    },
    
    'red':     {
        'throughput':30,
        'speed':3.75,
        'density':8
    },
    
    'blue':    {
        'throughput':45,
        'speed':5.625,
        'density':8
    }
}


# Science recipes
SR = {
    'red': {
        'copper_plate':1,
        'iron_gear':1
    },
    
    'green': {
        'transport_belt':1,
        'inserter':1
    },
    
    'blue': {
        'sulfur':1,
        'advanced_circuit':3,
        'engine_unit':2
    },
    
    'purple': {
        'rail':30,
        'electric_furnace':1,
        'productivity_module':1
    },
    
    'yellow': {
        'processing_unit':2,
        'flying_robot_frame':1,
        'low_density_structure':3
    },
}

