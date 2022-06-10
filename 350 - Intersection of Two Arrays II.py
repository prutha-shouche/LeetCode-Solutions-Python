# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 350. Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        a=[]
        i=j=0
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]==nums2[j]:
                a.append(nums1[i])
                i=i+1
                j=j+1
            elif nums1[i]<nums2[j]:
                i=i+1
            else:
                j=j+1
        return a
            

        
        
        
        