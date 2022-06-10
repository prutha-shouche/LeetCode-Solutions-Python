# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 367. Valid Perfect Square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        square_root=num ** 0.5 #gives square root of the number
        mod_1=square_root%1     #gives remainder
        if mod_1==0:
            return True
        else:
            return False
        
#example: 10                example: 16
# square_root=3.16228       square_root=4
#mod_1 = 0.16228            mod_1=0 
#return False               return True
        
        
        
            

        
        
        
        