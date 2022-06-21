# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 653. Two Sum IV - Input is a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # x+y=k
        # k=y-x equation logic
        n=set()
        def dfs(node):
            if not node:
                return False
            y=k-node.val
            if y in n:
                return True
            else:
                n.add(node.val)
            return (dfs(node.left) or dfs(node.right))
        return dfs(root)
        
            
            
        