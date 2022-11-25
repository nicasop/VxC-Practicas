#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:51:36 2022

@author: nicasop
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

#### dibujar la cara
p = np.zeros([11,11])
p[1,3:8] = 1
p[2,2:9] = 1
p[3:7,1] = 1
p[3:7,9] = 1

p[3:8,4:7] = 1
p[3:6,2] = 1
p[3:6,8] = 1
p[5:7,3] = 1
p[5:7,7] = 1 

p[9,3:8] = 1
p[8,2:4] = 1
p[8,7:9] = 1
p[7,1:3] = 1
p[7,8:10] = 1

plt.imshow(p,cmap='gray')

imDB = cv2.imread('./images/donBosco.jpg')
plt.figure()
plt.subplot(1,2,1)
plt.imshow(imDB,cmap='gray')

imDB_RGB = cv2.cvtColor(imDB,cv2.COLOR_BGR2RGB)
plt.subplot(1,2,2)
plt.imshow(imDB_RGB,cmap='gray')

R,G,B = cv2.split(imDB_RGB)

plt.figure()
plt.subplot(1,3,1)
plt.imshow(R,cmap='gray')
plt.title('Canal R')

plt.subplot(1,3,2)
plt.imshow(G,cmap='gray')
plt.title('Canal G')

plt.subplot(1,3,3)
plt.imshow(B,cmap='gray')
plt.title('Canal B')

imDB1 = imDB_RGB.copy()
plt.figure()
imDB1[160:170,105:115,0] = 0
imDB1[160:170,105:115,1] = 0
imDB1[160:170,105:115,2] = 0
# cv2.rectangle(imDB1,(105,160),(115,170),(0,0,0),-1)
plt.imshow(imDB1,cmap='gray')

imDB2 = imDB_RGB.copy()
plt.figure()
imDB2[160:170,105:115,0] = 255
imDB2[160:170,105:115,1] = 0
imDB2[160:170,105:115,2] = 0
# cv2.rectangle(imDB2,(105,160),(115,170),(255,0,0),-1)
plt.imshow(imDB2,cmap='gray')

pedazoRGB = imDB_RGB[100:104,50:54]
A = pedazoRGB[1,:,:]
print(A)