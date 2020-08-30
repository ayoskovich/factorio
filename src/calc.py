#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('run', './helpers.ipynb')


# In[ ]:


ips(CT['iron_gear'], CS['ass_2'])


# In[ ]:


ips(CT['pipe'], CS['steel_furnace'])


# In[ ]:


ips(CT['iron_plate'], CS['steel_furnace'])*36


# In[ ]:


ips(CT['iron_plate'], CS['steel_furnace'])


# In[ ]:


# Items needed to fill the belt
itf(
    CT['iron_plate'], 
    CS['steel_furnace'],
    BS['yellow']['throughput']
)


# In[ ]:


SR['blue']


# In[ ]:


# Science math (ish)
# 50 iron plates per second
# 120 copper plates per second
# 40 plastic per second
# 32 steel plates per second


# In[ ]:


.75*(1.20)*(1.20)


# In[ ]:


.75*1.40

