# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1356. Sort Integers by The Number of 1 Bits

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        #Approach 1
        ans=[]
        for num in arr:
            count=bin(num).count('1')
            ans.append([count,num])
        ans.sort()
        arr=[num for count,num in ans]
        return arr
    
    
# Approach -2    
#         arr.sort()
#         d={}
#         for i in arr:
#             count=bin(i).count('1')
#             if count not in d:
#                 d[count]=[i]
#             else:
#                 d[count].append(i)
#         res=[]
#         for i in sorted(d.keys()):
#             res.extend(d[i])
#         return res
        
        
            
        
        
        
                
                
        
            
                    
        
    
        
        

            
        
        
        
        
        
