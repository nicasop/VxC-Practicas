#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 02:56:09 2022

@author: nicasop
"""
import numpy as np
import funcionesVxC as f
import cv2
from matplotlib import pyplot as plt

Mat_ori = np.array([[130,400],
                    [250,500]])

Mat_des = np.array([[0,200],
                    [356,400]])

A1 = f.generar_A(Mat_ori, Mat_des)
print('---------------- A 1 ----------------')
print(A1)

Phi_1 = f.calcularPHI(A1)
print('---------------- PHI 1 ----------------')
print(Phi_1)


logo = np.load('./images/logoUPS.npy')
plt.figure()
plt.subplot(1,3,1)
plt.imshow(logo,cmap='gray')
plt.title("Original")

logo_ori = np.array([[0,0],[300,0],[300,400],[0,400]],np.float32)
logo_des = np.array([[100,0],[250,50],[300,300],[0,200]],np.float32)

A_logo = f.generar_A(logo_ori, logo_des)

Phi_2 = f.calcularPHI(A_logo)
print('matriz phi del logo')
print(Phi_2)

logo_trans = f.transformePerspective(logo, Phi_2, (301,301))
plt.subplot(1,3,2)
plt.imshow(logo_trans,cmap='gray')
plt.title('Manual')

M = cv2.getPerspectiveTransform(logo_ori, logo_des)
dst = cv2.warpPerspective(logo, M, (300,300))
print(dst[0][100])
print(logo)
plt.subplot(1,3,3 )
plt.imshow(dst,cmap='gray')
plt.title("opencv")