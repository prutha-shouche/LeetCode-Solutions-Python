# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 160. Intersection of Two Linked Lists


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #approach - add all values of listA in set
        #compare values of listB with list A and return intersection point
        first_set=set() #set stores unique values
        cur=headA
        while(cur):
            first_set.add(cur)
            cur=cur.next
        cur=headB
        while(cur):
            if cur in first_set:
                return cur
            cur=cur.next
                
        
        
        
        