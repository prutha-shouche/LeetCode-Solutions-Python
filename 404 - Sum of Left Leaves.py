# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 404. Sum of Left Leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        #DFS
        self.total=0
        def dfs(node,left):
            if not node:
                return
            dfs(node.left, True)
            dfs(node.right, False)
            if not node.right and not node.left and left:
                self.total=self.total+node.val
        dfs(root,False)
        return self.total
            
                
        
        
            
        
        
        
                
                
        
            
                    
        
    
        
        

            
        
        
        
        
        