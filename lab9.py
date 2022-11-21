#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install rioxarray


# In[8]:


pip install earthpy


# In[1]:


import os


# In[9]:


import matplotlib.pyplot as plt
import numpy as np
import rioxarray as rxr
import geopandas as gpd
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep


# In[3]:


pwd


# In[12]:


os.chdir("Documents/CPS NEU GIS/GIS6345/coldspringsfire")


# In[13]:


data = et.data.get_data('cold-springs-fire')


# In[14]:


os.chdir(os.path.join(et.io.HOME, 'earth-analytics', 'data'))


# In[15]:


naip_data_path = os.path.join("cold-springs-fire",
                              "naip",
                              "m_3910505_nw_13_1_20150919",
                              "crop",
                              "m_3910505_nw_13_1_20150919_crop.tif")

naip_data = rxr.open_rasterio(naip_data_path)

# View shape of the data
naip_data.shape


# In[16]:


naip_ndvi = es.normalized_diff(naip_data[3], naip_data[0])


# In[17]:


ep.plot_bands(naip_ndvi,
              cmap='PiYG',
              scale=False,
              vmin=-1, vmax=1,
              title="NAIP Derived NDVI\n 19 September 2015 - Cold Springs Fire, Colorado")
plt.show()


# In[ ]:




