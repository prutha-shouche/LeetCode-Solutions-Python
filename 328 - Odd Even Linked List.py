# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 328. Odd Even Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        odd=head
        even = odd.next
        evenList =even
       
        while(even and even.next):
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=odd.next
        odd.next=evenList
        return head
    