#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 23:23:29 2022

@author: nicasop
"""
import numpy as np
import cv2


## practica 1
def miCamaraPinhole(puntosUVW,phi):
  matriz_XY = []
  for fila in puntosUVW:
    V_uv = fila[0:2]
    ma_aux = np.dot(phi,V_uv)
    matriz_XY.append(np.round(ma_aux/fila[2]))
  return matriz_XY

def miCamaraPhinhole_1(puntosUVW,phi):
  num_filas = np.size(puntosUVW,0)
  matriz_XY = np.empty((num_filas,2))
  for i in range(num_filas):
    V_uv = puntosUVW[i][0:2]
    ma_aux = np.dot(V_uv,phi)
    matriz_XY[i]=(np.round(ma_aux/puntosUVW[i][2]))
  return matriz_XY

def calculeXY_Coordinate(coor_uvw,phi):
    V_uv = coor_uvw[0:2]
    ma_aux = np.dot(V_uv,phi)
    return np.round(ma_aux/coor_uvw[2])

def miCamaraPinhole2(PuntosUVW,Phi):
    matriz_XY = np.apply_along_axis(calculeXY_Coordinate, axis=1, arr=PuntosUVW,phi=Phi)
    return matriz_XY

def miCamaraPinhole3(PuntosUVW,Phi):
    matriz_XY = np.apply_along_axis(lambda coor,phi: np.round(np.dot(phi,coor[0:2])/coor[2]) , axis=1, arr=PuntosUVW,phi=Phi)
    return matriz_XY

## practica 2
def generar_A(O,D):
    A = []
    for i in range(len(O)):
        v_1=[-1*O[i][0],-1*O[i][1],-1,0,0,0,O[i][0]*D[i][0],O[i][1]*D[i][0],D[i][0]]
        v_2=[0,0,0,-1*O[i][0],-1*O[i][1],-1,O[i][0]*D[i][1],O[i][1]*D[i][1],D[i][1]]
        A.append(v_1)
        A.append(v_2)
    return A

def calcularPHI(A):
    B = np.linalg.svd(A)
    Vt = B[2]
    V = np.transpose(Vt)
    p = V[:,len(V[0])-1]
    phi = np.reshape(p,(3,3))
    return phi

def transformePerspective(img,PHI,tam):
    img_trns = np.zeros(tam)
    for i in range(len(img)):
        for j in range(len(img[i])):
            uv = np.array([j,i,1],np.float64)
            aux = np.dot(PHI,uv)
            xy = np.uint8(np.round([aux[0]/aux[2],aux[1]/aux[2]]))
            xy = np.round([aux[0]/aux[2],aux[1]/aux[2]])
            img_trns[int(xy[1])][int(xy[0])] = img[i][j]
    return img_trns


## practica 4
def miColor2Gris(im, alfa, beta, gamma):
  im = np.float64(im)
  R,G,B = cv2.split(im)
  P = (R*alfa+G*beta+B*gamma)
  return np.uint8(P)    

def miGris2byn(P,umbral):
    X = np.zeros(np.shape(P))
    for i in range(len(P)):
        for j in range (len(P[i])):
            if (P[i][j] > umbral):
                X[i][j] = 1
            else:
                X[i][j] = 0
    return X
#[1,1,1,1]
##practica 5
def miHistograma(P):
    hk = np.zeros((256,), dtype=int)
    # unique, counts = np.unique(P, return_counts=True)
    for i in range(len(hk)):
        hk[i] = np.count_nonzero(P == i)
    return hk

def miHPA(P):
    ck = np.zeros((256,),dtype=float)
    hist_P = miHistograma(P)
    I = len(P)
    J = len(P[0])
    for i in range(len(hist_P)):
        ck[i] = (sumValues(hist_P,i))/(I*J)
    return ck
            
def sumValues(vec,pos):
    if pos < len(vec):
        suma = 0
        for i in range(pos+1):
            suma += vec[i]
    return suma

def miEcualizador(P):
    # X = P
    X = np.zeros((len(P),len(P[0])))
    hpa = miHPA(P)
    for i in range(len(P)):
        for j in range(len(P[i])):
            num = 255*hpa[P[i][j]]
            X[i][j] = round(num)
    return X

def miNormalizador(P):
    X = np.zeros((len(P),len(P[0])))
    minimo = np.amin(P)
    maximo = np.amax(P)
    m = calculate_slope(minimo, maximo)
    for i in range(len(P)):
        for j in range(len(P[i])):
            X[i][j] = round(P[i][j]*m - m*minimo)
    return np.uint8(X)
            
def calculate_slope(min,max):
    return 255/(max-min)

def miBlaqueador(P):
    X = np.zeros((len(P),len(P[0])))
    mean = P.mean()
    std = P.std()
    for i in range(len(P)):
        for j in range(len(P[i])):
            X[i][j] = (P[i][j]-mean)/std
    return X
    
    
    
    
    
    