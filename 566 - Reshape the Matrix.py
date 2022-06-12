# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 566. Reshape the Matrix

import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        #Approach 1
        x=np.array(mat)
        shape=(r,c)
        if r*c!=len(mat)*len(mat[0]):
            return mat
        else:
            return x.reshape(shape)
   
import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        #Approach 2
        x=np.array(mat)
        shape=(r,c)
        try:
            return x.reshape(shape)
        except ValueError:
            return mat

        
        
        
        