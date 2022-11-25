#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 22:48:20 2022

@author: nicasop
"""

import cv2
from matplotlib import pyplot as plt
import funcionesVxC as f

imLena = cv2.imread("./images/lena.jpg")
imLena_RGB = cv2.cvtColor(imLena,cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(imLena_RGB,cmap='gray')

lenaP1 = f.miColor2Gris(imLena_RGB,0.8,0.1,0.1)
lenaP2 = f.miColor2Gris(imLena_RGB,0.1,0.8,0.1)
lenaP3 = f.miColor2Gris(imLena_RGB,0.1,0.1,0.8)
plt.figure()
plt.subplot(1,3,1)
plt.imshow(lenaP1,cmap='gray')
plt.title("0.8-0.1-0.1")

plt.subplot(1,3,2)
plt.imshow(lenaP2,cmap='gray')
plt.title("0.1-0.8-0.1")

plt.subplot(1,3,3)
plt.imshow(lenaP3,cmap='gray')
plt.title("0.1-0.1-0.8")

lena_gris = cv2.cvtColor(imLena_RGB,cv2.COLOR_RGB2GRAY)
plt.figure()
plt.subplot(1,2,1)
plt.imshow(imLena_RGB,cmap='gray')
plt.title('Original')
plt.subplot(1,2,2)
plt.imshow(lena_gris,cmap='gray')
plt.title('Escala de grises')

lena_byn1 = f.miGris2byn(lena_gris, 50)
lena_byn2 = f.miGris2byn(lena_gris, 180) 
plt.figure()
plt.subplot(1,2,1)
plt.imshow(lena_byn1,cmap='gray')
plt.title('umbral=50')
plt.subplot(1,2,2)
plt.imshow(lena_byn2,cmap='gray')
plt.title('umbral=180')

umbral , X = cv2.threshold(lena_gris,0,255,cv2.THRESH_OTSU)

plt.figure()
plt.imshow(X,cmap='gray')
plt.title('BInarización Otzu')
