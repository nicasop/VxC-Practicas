#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 23:06:36 2022

@author: nicasop
"""
import funcionesVxC as f
import numpy as np
import time
import matplotlib.pyplot as plt

puntosUVW = np.array([[12,10,5],
                      [8,21,13]])
phi = np.array([[26,0],[0,44]])

ini_1 = time.time()
mat = f.miCamaraPinhole(puntosUVW,phi)
fin_1 = time.time()
print('Funcion camaraPinhole')
print(mat)
print('Tiempo de ejecucion: ',fin_1-ini_1)

mat1 = f.miCamaraPinhole3(puntosUVW,phi)
print('Funcion camaraPinhole3')
print(mat1)

coor_fig = np.array([[2,0,10],
                     [2,3,13],
                     [2,6,10],
                     [2,3,7],
                     [7,0,10],
                     [7,3,13],
                     [7,6,10],
                     [7,3,7]])

phi_coor = np.array([[20,0],[0,18]])

ini1 = time.time()
res1 = f.miCamaraPinhole(coor_fig,phi_coor)
fin1 = time.time()
print("RESPUESTA 1")
print(res1)
print("Tiempo de ejecución: ",fin1 - ini1)

ini2 = time.time()
res2 = f.miCamaraPinhole3(coor_fig,phi_coor)
fin2 = time.time()
print("RESPUESTA 2")
print(res2)
print("Tiempo de ejecución: ",fin2 - ini2)

##### GRAFICA
##puntos
# plt.plot(res2[:,0],-1*res2[:,1],"o")

#### Cuadricula izquierda
plt.plot([4,3],[0,-4],color="b")
plt.scatter([4,3],[0,-4],color="b")
plt.plot([4,6],[-11,-8],color="b")
plt.scatter([4,6],[-11,-8],color="b")
plt.plot([3,4],[-4,-11],color="b")
plt.scatter([3,4],[-4,-11],color="b")
plt.plot([4,6],[0,-8],color="b")
plt.scatter([4,6],[0,-8],color="b")


#### Cuadricula derecha
plt.plot([11,14],[-4,0],color="b")
plt.scatter([11,14],[-4,0],color="b")
plt.plot([14,20],[-11,-8],color="b")
plt.scatter([14,20],[-11,-8],color="b")
plt.plot([11,14],[-4,-11],color="b")
plt.scatter([11,14],[-4,-11],color="b")
plt.plot([14,20],[0,-8],color="b")
plt.scatter([14,20],[0,-8],color="b")

#### Unir cuadriculas
plt.plot([4,14],[0,0],color="b")
plt.scatter([4,14],[0,0],color="b")
plt.plot([3,11],[-4,-4],color="b")
plt.scatter([3,11],[-4,-4],color="b")
plt.plot([6,20],[-8,-8],color="b")
plt.scatter([6,20],[-8,-8],color="b")
plt.plot([4,14],[-11,-11],color="b")
plt.scatter([4,14],[-11,-11],color="b")

#### Mostrar grafica
plt.show()
