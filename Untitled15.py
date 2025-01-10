#!/usr/bin/env python
# coding: utf-8

# In[5]:


x = np.array([40,67,57,90])
print(x)
print(type(x))
print(x.dtype)


# In[7]:


import numpy as np


# In[15]:


#numpy array
x = np.array([40,67,57,90])
print(x)
print(type(x))
print(x.dtype)


# In[11]:


x = np.array([40,67,57,9.0])
print(x)
print(type(x))
print(x.dtype)


# In[13]:


x = np.array(["A",67,57,9.0])
print(x)
print(type(x))
print(x.dtype)


# In[17]:


a2 = np.array([[10,20],[30,60]])
print(a2)
print(type(a2))
print(a2.dtype)


# In[21]:


a = np.array([10,20,30,60])
print(a)
print(type(a))
print(a.dtype)


# In[29]:


#reshaping an array
a = np.array([10,20,30,40])
b = a.reshape(2,2)
print(b)
print(b.shape)


# In[47]:


#create an array with arange()
c = np.arange(2522)
print(c)
type(c)


# In[53]:


#use of around()
d = np.array([1.2345, 3.2067,4.91236])
np.around(d,2)


# In[55]:


#use of np.sqrt()
print(np.sqrt(d))


# In[57]:


print(np.around(np.sqrt(d),2))


# In[59]:


a1 = np.array([[3,4,5,6],[7,6,8,9]])
a1_copy1 = a1.astype(float)
a1_copy1.dtype


# In[63]:


a1 = np.array([[3,4,5,6],[7,6,8,np.NAN]])
print(a1)
a1.dtype


# In[65]:


a1 = np.array([[3,4,5,6],[7,6,8,np.NaN]])
print(a1)
a1.dtype


# In[69]:


a1_copy1 = a1.astype(str)
print(a1_copy1)
a1_copy1.dtype


# In[71]:


a2 = np.array([[3,4,5,6],[7,8,9,6]])
a2


# In[73]:


print(a2.sum(axis = 1))
print(a2.sum(axis=0))


# In[75]:


np.sqrt(a2)


# In[77]:


#find the mean value along row and col
print(np.mean(a2, axis =1))
print(np.mean(a2, axis =0))


# In[79]:


#find the mean value along row and col
print(a2)
print(np.mean(a2, axis =1))
print(np.mean(a2, axis =0))


# In[81]:


a3 = np.array([[3,4,5,6],[7,6,8,9],[1,2,3,4]])
print(a3)
np.fill_diagonal(a3,0)
print(a3)


# In[85]:


A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
C = np.matmul(A, B)
print(C)


# In[87]:


print(A.T)
print(B.T)


# In[95]:


#Accessing the array elements
a4 = np.array([[3,4,5,6],[7,6,8,9],[1,2,3,4],[4,5,6,7]])
a4


# In[99]:


#silicing of array
a4[1:3,0:2]


# In[ ]:




