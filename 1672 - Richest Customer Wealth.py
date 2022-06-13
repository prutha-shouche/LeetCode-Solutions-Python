# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1672. Richest Customer Wealth


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth=0
        for i in range(len(accounts)):
            maxwealth=max(sum(accounts[i]), maxwealth)
        return maxwealth
        
        
        