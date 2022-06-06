# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 83. Remove Duplicates from Sorted List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempNode=head
        while(tempNode):
            if tempNode.next and tempNode.val==tempNode.next.val:
                tempNode.next=tempNode.next.next
            else:
                tempNode=tempNode.next
        return head
                
            
            
        
        