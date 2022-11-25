#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 02:25:18 2022

@author: nicasop
"""

import cv2
import numpy as np
import funcionesVxC as f
from matplotlib import pyplot as plt

P1 = cv2.imread('./images/foto1.jpg')
P1 = cv2.cvtColor(P1, cv2.COLOR_BGR2GRAY)

P2 = cv2.imread('./images/foto2.jpg')
P2 = cv2.cvtColor(P2, cv2.COLOR_BGR2GRAY)

P3 = cv2.imread('./images/foto3.jpg')
P3 = cv2.cvtColor(P3, cv2.COLOR_BGR2GRAY)

P4 = cv2.imread('./images/foto4.jpg')
P4 = cv2.cvtColor(P4, cv2.COLOR_BGR2GRAY)

hist_p1 = f.miHistograma(P1)
hist_p2 = f.miHistograma(P2)
hist_p3 = f.miHistograma(P3)
hist_p4 = f.miHistograma(P4)


hpa_P1 = f.miHPA(P1)
hpa_P2 = f.miHPA(P2)
hpa_P3 = f.miHPA(P3)
hpa_P4 = f.miHPA(P4)

plt.figure()
## imagenes
plt.subplot(3,4,1)
plt.imshow(P1,cmap='gray')
plt.subplot(3,4,2)
plt.imshow(P2,cmap='gray')
plt.subplot(3,4,3)
plt.imshow(P3,cmap='gray')
plt.subplot(3,4,4)
plt.imshow(P4,cmap='gray')

## histogramas
plt.subplot(3,4,5)
plt.plot(hist_p1)
plt.subplot(3,4,6)
plt.plot(hist_p2)
plt.subplot(3,4,7)
plt.plot(hist_p3)
plt.subplot(3,4,8)
plt.plot(hist_p4)

## HPA
plt.subplot(3,4,9)
plt.plot(hpa_P1)
plt.subplot(3,4,10)
plt.plot(hpa_P2)
plt.subplot(3,4,11)
plt.plot(hpa_P3)
plt.subplot(3,4,12)
plt.plot(hpa_P4)


EP1 = f.miEcualizador(P1)
EP2 = f.miEcualizador(P2)
EP3 = f.miEcualizador(P3)
EP4 = f.miEcualizador(P4)

hist_ep1 = f.miHistograma(EP1)
hist_ep2 = f.miHistograma(EP2)
hist_ep3 = f.miHistograma(EP3)
hist_ep4 = f.miHistograma(EP4)

hpa_ep1 = f.miHPA(EP1)
hpa_ep2 = f.miHPA(EP2)
hpa_ep3 = f.miHPA(EP3)
hpa_ep4 = f.miHPA(EP4)

plt.figure()
## imagenes
plt.subplot(3,4,1)
plt.imshow(EP1,cmap='gray')
plt.subplot(3,4,2)
plt.imshow(EP2,cmap='gray')
plt.subplot(3,4,3)
plt.imshow(EP3,cmap='gray')
plt.subplot(3,4,4)
plt.imshow(EP4,cmap='gray')

#Histograma
plt.subplot(3,4,5)
plt.plot(hist_ep1)
plt.subplot(3,4,6)
plt.plot(hist_ep2)
plt.subplot(3,4,7)
plt.plot(hist_ep3)
plt.subplot(3,4,8)
plt.plot(hist_ep4)

## HPA
plt.subplot(3,4,9)
plt.plot(hpa_ep1)
plt.subplot(3,4,10)
plt.plot(hpa_ep2)
plt.subplot(3,4,11)
plt.plot(hpa_ep3)
plt.subplot(3,4,12)
plt.plot(hpa_ep4)


P = np.array([[199,182,202],[86,36,166],[151,77,141],[199,240,9],[41,22,189],[48,33,208]])
X_n = f.miNormalizador(P)
print(X_n)
X_b = f.miBlaqueador(P)
print(X_b)