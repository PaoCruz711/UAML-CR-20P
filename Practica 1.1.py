#!/usr/bin/env python
# coding: utf-8

# Está función recibirá un entero (n) y devolverá un
# diccionario que representa la gráfica Kn.
# 

# In[100]:


#CREACION DE GRAFO
#Obtendremos el numero de nodos que tendra la grafica
n = int(input('Ingresa un numero entero: ')) #Leemos desde teclado
lista1 = list() #Creamos una lista
for i in range(1,n+1):#creamos una lista inmutable 
    lista1.append(i)
print(list_1)


# #Crear diccionario vacio
# d5 = {} 
# print(d5)
# 

# In[104]:


#Crear diccionario vacio en el cual agregaremos los elementos de la lista1
diccionario = {} 
print(d5)
for i in range(1,n+1):
    listaTemp = list(lista1)#Es necesario crear una lista temporal para poder copiar el contenido de la lista1
    listaTemp.remove(i)#removemos i para evitar la repetición en el diccionario
    llave = {i:listaTemp}
    diccionario.update(llave)

print(diccionario)


# #CALCULAR LOS GRADOS DE ENTRADA

# In[105]:





# In[80]:





# In[107]:





# In[109]:


x2 = list()
y2 = list()

suma = sum(grafica_distr_norm.values())

for i in grafica_distr_norm:
    x2.append(grafica_istr_norm[i])
    valor = i/s
    y2.append(valor)
plt.plot(x2,y2)
plt.title('Distribución Normalizada de Grados de Entrada')
plt.xlabel('grado nodal')
plt.ylabel('proporción de nodos')
plt.show()


# In[ ]:





# In[ ]:




