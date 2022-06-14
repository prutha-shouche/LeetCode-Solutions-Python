# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1572. Matrix Diagonal Sum


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i==j or i+j==len(mat[0])-1:
                    total+=mat[i][j]              
        return total
                
    
        
        

            
        
        
        
        
        