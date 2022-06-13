# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 202. Happy Number


class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        while True:
            if n==1:
                return True
            total=0
            num=n
            while(num):
                total+=(num%10)**2
                num=num//10

            if total not in a:
                a.add(total)
                n=total
            else:
                return False
        return True
    

            
        
        
        
        
        