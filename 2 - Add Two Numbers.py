# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        #approach 1
        total=0
        carry=0
        ans=ListNode(None)
        pointer=ans
        while(l1!=None or l2!=None):
            total=carry
            if l1!=None:
                total=total+l1.val
                l1=l1.next
            if l2!=None:
                total=total+l2.val
                l2=l2.next
            carry=int(total/10)
            pointer.next=ListNode(total%10)
            pointer=pointer.next
        if carry>0:
            pointer.next=ListNode(carry)
        return ans.next
                  
       #approach 2 
#         dummyHead = ListNode(0)
#         carry =0
#         curr=dummyHead
#         while l1 or l2:
#             if l1:
#                 l1_val=l1.val
#             else :
#                 l1_val=0
#             if l2:
#                 l2_val=l2.val
#             else :
#                 l2_val=0
#             add=l1_val+l2_val+carry
            
#             curr.next=ListNode(add %10)
#             curr=curr.next
#             carry=add//10
#             if l1:
#                 l1=l1.next
#             if l2:
#                 l2=l2.next
#         if carry:
#             curr.next=ListNode(carry)
#         return dummyHead.next
            
        
            
                
        
        
        
        