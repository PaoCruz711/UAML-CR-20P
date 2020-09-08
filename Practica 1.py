#!/usr/bin/env python
# coding: utf-8

# NODOS/NODOS ADYACENTES
# 0/Alice 1/Carlos 2/Beto 3/Jorge 4/Enrique 5/Rosa 6/Irene 7/Carmen 8/David 9/Mónica

# In[16]:


#Creación de diccionario
red= {0:[1,2,7,8,9], 1:[0,8,9], 2:[0,3], 3:[2,4,5,6], 4:[5,6],  5:[3,4,6], 6:[3,4,5],  7:[0,9],  8:[0,1], 9:[0,1,7]}
       


# In[23]:


#Función número nodos...
nodos= list()
for key in red:
    nodos.append(key)
print(len(nodos))


# In[33]:


#Calcula grados
M=0
for cont in red:
    print('Nodo:',cont,'Grado:',len(red[cont]))
    if M<len(red[cont]):
        M=len(red[cont])


# In[34]:


#Grado máximo
print(M)


# In[ ]:




