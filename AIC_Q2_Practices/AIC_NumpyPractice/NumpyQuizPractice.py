# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 23:18:54 2021

@author: BlueBottles
"""

import numpy as np

np_arr = np.array([0,1,2.5,3,4,5,6,7,8,9])
np_arr1 = np.array(range(6)).reshape(-1,2)
np_arr[3:6]= range(3)
print(np_arr.strides)
np_flt = np_arr.astype('i2',casting='unsafe')
# np.reshape(np_arr1,(2,3))
# reshaped = np_arr1.reshape((2,3))
resized = np.resize(np_arr1,(2,3))
# print(reshaped)
# print(resized)
print(np_arr1)
