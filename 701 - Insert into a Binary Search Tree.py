# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 701. Insert into a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        def insert(node,val):
            if val<node.val:
                if not node.left:
                    node.left=TreeNode(val)
                else:
                    insert(node.left,val)
            else:
                if not node.right:
                    node.right=TreeNode(val)
                else:
                    insert(node.right,val)
                
        insert(root,val)
        return root
        
        
            
            
        