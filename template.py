# -*- coding: utf-8 -*-
"""
Created on %(20170712)s

@author: %(lika)s
"""
from PIL import Image
import numpy as np
m = np.array(Image.open('C:/Users/Lika/Desktop/11.jpg').convert('L')).astype('float')

depth =10.  #构建虚拟虚拟深度值
grad = np.gradient(m)
grad_x ,grad_y = grad
grad_x = grad_x*depth/100.  #对梯度归一化
grad_y = grad_y*depth/100.
A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1./ A

vec_el = np.pi/1.5
vec_az = np.pi/3
dx = np.cos(vec_el)*np.cos(vec_az)
dy = np.cos(vec_el)*np.cos(vec_az)
dz = np.sin(vec_el)

b = 255*(dx*uni_x + uni_y +dz*uni_z)
b = b.clip(0,255)
im =Image.fromarray(b.astype('uint8'))
im.save('C:/Users/Lika/Desktop/3.JPG')
