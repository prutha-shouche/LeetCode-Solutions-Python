# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Approach - Using Recursion
        in_list=[]
        if not root:
            return
        if root.left:
            in_list+=self.inorderTraversal(root.left)
        in_list.append(root.val)
        if root.right:
            in_list+=self.inorderTraversal(root.right)
        return in_list
        
        
      
        
        
            
                    
        
    
        
        

            
        
        
        
        
        