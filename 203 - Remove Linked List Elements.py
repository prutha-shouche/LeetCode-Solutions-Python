# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 203. Remove Linked List Elements


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result = None
        while head:
            if not result and head.val != val:
                result = head   
            if head.next and head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return result
    
        
        

            
        
        
        
        
        