# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 496. Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Approach 1 - time comp O(N)
        nums1indx={n:i for i,n in enumerate(nums1)}
        res=[-1]*len(nums1)
        stack=[]
        
        for i in range(len(nums2)):
            cur=nums2[i]
            while stack and cur>stack[-1]:
                val=stack.pop()
                idx=nums1indx[val]
                res[idx]=cur
            if cur in nums1indx:
                stack.append(cur)
        return res
                          
        
        
        
        
        #Approach 2
        #O(N^2) time complexity
        # nums1indx={n:i for i,n in enumerate(nums1)}
        # res=[-1]*len(nums1)
        
#         for i in range(len(nums2)):
#             if nums2[i] not in nums1indx:
#                 continue
#             for j in range(i+1,len(nums2)):
#                 if nums2[j]>nums2[i]:
#                     idx=nums1indx[nums2[i]]
#                     res[idx]=nums2[j]
#                     break
#         return res
    
    
    
#Approach 3
#         ans = []
#         for i in nums1:
#             for j in nums2[nums2.index(i):]:
#                 if j > i:
#                     ans.append(j)
#                     break
#             else:
#                 ans.append(-1)
#         return ans
                
        
        
        
        
            
        
            
        
        
        

            
        
        
        
        
        