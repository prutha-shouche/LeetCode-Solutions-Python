# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 191. Number of 1 Bits

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Approach 2 - optimized approach
        maxprofit=0
        curprice = prices[0]
        for i in range(1,len(prices)):
            maxprofit=max(maxprofit, prices[i]-curprice)
            curprice=min(curprice, prices[i])
        return maxprofit
    
    
        #Approach 1 (time comp - O(n^2) (Time limit exceeded))
#         maxprofit=0
#         for i in range(0,len(prices)):
#             for j in range(i+1,len(prices)):
#                 if j>i:
#                     maxprofit = max(maxprofit, prices[j]-prices[i])
#                 else:
#                     maxprofit=0
#         return maxprofit
        
        
            
            
         


        
        
        