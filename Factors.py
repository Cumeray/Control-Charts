#!/usr/bin/env python
# coding: utf-8
# Created by: ernesto L. Garcia C., Phd
# Appaloosa Engineering LLC
 
# In[1]:


import pandas as pd
import numpy as np
import math


# ### Creating a data table with factors $d_2$ and $d_3$

# Source:
# Acheson, J Duncan(1986) *Quality Control and Industrial Statistics*, Irwin, 5th Ed. ISBN: 0-256-03535-0. p. 1025.

# In[2]:


dt={'n':[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],
    'd2':[1.128,1.693,2.059,2.326,2.534,2.704,2.847,2.97,3.078,3.173,3.258,3.336,3.407,3.472,3.532,3.588,3.64,
          3.689,3.735,3.778,3.819,3.858,3.895,3.931],
    'd3':[0.853,0.888,0.88,0.864,0.848,0.833,0.82,0.808,0.797,0.787,0.778,0.77,0.762,0.755,0.749,0.743,0.738,0.733,
          0.729,0.724,0.72,0.716,0.712,0.709]}


# In[3]:


dtable=pd.DataFrame(dt, columns=['n','d2','d3'])


# In[16]:


#print(dtable)


# ## Calculation of $c_4$
# $c_4=\sqrt{\frac{2}{n-1}}\frac{\Gamma{\frac{n}{2}}}{\Gamma{\frac{n-1}{2}}}$

# In[5]:


def c4(n):
    c4=math.sqrt(2/(n-1))*math.gamma(n/2)/math.gamma((n-1)/2)
    return c4


# Return of $d_2$

# In[17]:


def d2(n):
    if n > 25:
        d2=4
    else:
        d2=dtable.d2[n-2]
    return d2


# Return of $d_3$

# In[24]:


def d3(n):
    if n > 25:
        d3=0.7
    else:
        d3=dtable.d3[n-2]
    return d3

