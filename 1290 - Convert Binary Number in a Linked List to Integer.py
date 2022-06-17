# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1290. Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        tempNode=head
        a=[]
        while tempNode:
            a.append(tempNode.val) 
            tempNode=tempNode.next
        n=len(a)-1
        sum=0
        for i in range(len(a)):
            sum=sum+(a[n-i]*(2**i))
        return sum
        
        
        
                
                
        
            
                    
        
    
        
        

            
        
        
        
        
        