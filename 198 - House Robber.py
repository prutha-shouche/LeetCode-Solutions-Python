# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 198. House Robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        #Approach-Optimised
        rob1,rob2=0,0
        for n in nums:
            temp=max(rob1+n, rob2)
            rob1=rob2
            rob2=temp
        return rob2
    #Approach 1
#         n=len(nums)
#         if not nums:
#             return 0
#         if n<=2:
#             return max(nums)
        
#         dp=[0]*n

#         dp[0]=nums[0]
#         dp[1]=max(nums[0],nums[1])
        
#         for i in range(2,len(nums)):
#             dp[i]=max(dp[i-1],nums[i]+dp[i-2])
#         return dp[-1]
        
        
        
        #Approach 1 - Using Recursion
#         a = []
#         if not root:
#             return 
#         if root.left:
#             a +=self. postorderTraversal(root.left)     
#         if root.right:
#             a += self.postorderTraversal(root.right)     
#         a.append(root.val)
#         return a
                
        
        
      
        
        
            
                    
        
    
        
        

            
        
        
        
        
        