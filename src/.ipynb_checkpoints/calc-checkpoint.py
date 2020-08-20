#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ips(c_time, c_speed):
    """ Computes items per second from a recipe and 
        assembler.
    
    c_time (float): Crafting time of recipe
    c_speed (float): Crafting speed of the assembler
    """
    return 1 / (c_time / c_speed)


# In[2]:


ips(c_time=3.2, c_speed=2)


# In[4]:


ips(.5, .75)


# In[ ]:


testing

