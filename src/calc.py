#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('run', './helpers.ipynb')


# In[2]:


ips(T['iron_plate'], S['steel_furnace'])


# In[3]:


ips(T['iron_plate'], S['stone_furnace'])


# In[4]:


ips(T['iron_plate'], S['steel_furnace'])


# In[5]:


B['yellow'] / ips(T['iron_plate'], S['steel_furnace'])


# In[6]:


B['yellow'] / ips(T['iron_plate'], S['steel_furnace'])


# In[7]:


itf(
    ips(T['iron_plate'], S['steel_furnace']),
    B['yellow']
)

