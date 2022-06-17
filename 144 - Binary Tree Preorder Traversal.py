# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 20. Valid Parentheses


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Approach - Using Recursion
        pre_list=[]
        if not root:
            return
        pre_list.append(root.val)
        if root.left:
            pre_list+=self.preorderTraversal(root.left)
        if root.right:
            pre_list+=self.preorderTraversal(root.right)
        return pre_list
        
        
      
        
        
            
                    
        
    
        
        

            
        
        
        
        
        