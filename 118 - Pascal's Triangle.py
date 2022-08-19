# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 118. Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        
        for i in range(numRows-1): 
            temp=[0]+res[-1]+[0] #adding 0 to start and end of prev row
            row=[]
            for j in range(len(res[-1])+1): #length of the prvious row (len(res[-1])+ 1
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return res
                
                
        
            
                    
        
    
        
        

            
        
        
        
        
        
