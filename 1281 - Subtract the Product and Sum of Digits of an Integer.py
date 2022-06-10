# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 350. Intersection of Two Arrays II

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a=[]
        sum=0
        prdt=1
        while(n!=0):
            a.append(n%10)
            n=n//10
        for i in range(0,len(a)):
            sum=sum+a[i]
            prdt=prdt*a[i]
        return prdt-sum

        
            
        
        
            

        
        
        
        