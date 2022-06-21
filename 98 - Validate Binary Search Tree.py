# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 98. Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # - infinity, +infinity setting min and max values. Keep updating them. 
        # Min < Value < Max
        # -infi<3<5 for left sub tree
        # 5<7<+infi for right sub tree
        def valid(node,left,right):
            if not node:
                return True
            if not (node.val<right and node.val>left):
                return False
            return (valid(node.left, left,node.val)and
                    (valid(node.right,node.val,right)))#1st (keep left val as it is and update right val) and 2nd (keep right val as it is and update left node val) 
        return valid(root, float("-inf"), float("+inf"))
        
            
            
        