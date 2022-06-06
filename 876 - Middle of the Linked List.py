# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 876. Middle of the Linked List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach- two pointers - slow and fast
        #when fast pointer reaches the end, slow pointer will reach middle
        slow=fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        return slow
            
        