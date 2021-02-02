
# coding: utf-8

# In[35]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[36]:


x = [1, 2, -3, 4, 5]
y = [6, -7, 8, -9, 10]


# In[37]:


plt.legend("x en fonction de y")
plt.plot(x, y)


# In[38]:


fig, ax = plt.subplots()
ax.plot(x,y)


# In[39]:


plt.show()


# In[40]:


x = np.array([1, 2, 3, 4, 5])


# In[41]:


x = np.linspace(0, 10, 45)
y = np.cos(x)


# In[42]:


fig, ax = plt.subplots()
ax.plot(x, y)


# In[43]:


def f_tan(x):
    return x + np.tan(2*x -1)


# In[44]:


x = np.linspace(0, 10, 45)
y = f_tan(x)


# In[55]:


fig, ax = plt.subplots()
ax.plot(x, y)


# In[51]:


#fig, ax = plt.subplots(2, 3)
#ax[1][-1].plot(x, y)


# In[56]:


fig.legend


# In[57]:


ax


# In[58]:


a = 90


# In[59]:


x = np.cos(a)
y = np.sin(a)


# In[60]:


fig, ax = plt.subplots()
ax.plot(x, y)

