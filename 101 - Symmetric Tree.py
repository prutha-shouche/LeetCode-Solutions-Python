# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.symmetry(root.left,root.right)
    def symmetry(self,r1,r2):
        if r1 and r2: #not none
            return r1.val==r2.val and self.symmetry(r1.left,r2.right) and self.symmetry(r1.right,r2.left)
        return r1==r2
            
            
        
        
        
                
                
        
            
                    
        
    
        
        

            
        
        
        
        
        