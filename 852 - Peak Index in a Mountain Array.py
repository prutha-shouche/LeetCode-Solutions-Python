# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 852. Peak Index in a Mountain Array


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            print(mid)
            if mid + 1 < n and arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left