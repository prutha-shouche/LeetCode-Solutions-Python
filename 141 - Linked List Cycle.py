# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 141. Linked List Cycle


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Turtle-Hare Problem
        #In this problem, turtle moves one step and hare moves 2 steps. 
        #If at any point they coincide, then cycle exist.
        turtle=head
        hare=head
        while(turtle and hare and hare.next):
            turtle=turtle.next
            hare=hare.next.next
            if(turtle==hare):
                return True
        return False
        