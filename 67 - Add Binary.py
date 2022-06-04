# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        result=[]
        carry=0
        while(i>=0 or j>=0 or carry):
            sum=carry
            if (i>=0):
                sum=sum+int(a[i])
                i=i-1
            if (j>=0):
                sum=sum+int(b[j])
                j=j-1
            result.append(str(sum%2))
            carry=sum//2
        return ''.join(reversed(result))