# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1491. Average Salary Excluding the Minimum and Maximum Salary

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n=len(salary)-1
        sum=0
        total=len(salary)-2
        for i in range(1,n):
            sum=sum+salary[i]
        avg=sum/total
        return avg
        

    
        
                
            
            
        