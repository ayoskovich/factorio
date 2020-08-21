#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('run', './helpers.ipynb')


# In[2]:


ips(CT['iron_gear'], CS['ass_2'])


# In[3]:


ips(CT['pipe'], CS['steel_furnace'])


# In[18]:


ips(CT['iron_plate'], CS['steel_furnace'])*36


# In[27]:


itf(
    CT['iron_plate'], 
    CS['steel_furnace'],
    15
)


# In[26]:


ips(CT['iron_plate'], CS['steel_furnace'])


# In[4]:


itf(
    CT['iron_plate'], 
    CS['steel_furnace'],
    BS['yellow']
)


# In[8]:


SR['blue']


# In[9]:


# Science math (ish)
# 50 iron plates per second
# 120 copper plates per second
# 40 plastic per second
# 32 steel plates per second


# In[23]:


.75*(1.20)*(1.20)


# In[24]:


.75*1.40


# An assembler with 2 * 20% speed modules applies a 40% increase ONCE, not a 20% increase twice.
