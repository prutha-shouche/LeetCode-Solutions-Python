# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1790. Check if One String Swap Can Make Strings Equal

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c=0
        a={}
        for i in range(len(s1)):
            if s1[i]==s2[i]:
                continue
            else:
                a[c]=i
                c=c+1
        if c==0:
            return True
        elif c==2:
            if(s1[a[0]]==s2[a[1]] and s1[a[1]]==s2[a[0]]):
                return True
        return False
            
        