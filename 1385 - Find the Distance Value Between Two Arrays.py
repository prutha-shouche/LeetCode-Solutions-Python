# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1385. Find the Distance Value Between Two Arrays


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
  
        min_dist=0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                diff=abs(arr1[i]-arr2[j])
                if diff<=d:
                    min_dist=min_dist+1
                    break
        return len(arr1)-(min_dist)
        