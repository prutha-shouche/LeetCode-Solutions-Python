# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Approach 2 - Using Stacks
        if(not root):
            return
        
        ans = []
        s1 = []
        s2 = []

        s1.append(root)

        while(s1):
            x = s1[-1]
            s1.pop()
            s2.append(x)

            if(x.left):
                s1.append(x.left)
            if(x.right):
                s1.append(x.right)
        
        while(s2):
            y = s2[-1]
            s2.pop()
            ans.append(y.val)
        return ans
            
        
        #Approach 1 - Using Recursion
#         a = []
#         if not root:
#             return 
#         if root.left:
#             a +=self. postorderTraversal(root.left)     
#         if root.right:
#             a += self.postorderTraversal(root.right)     
#         a.append(root.val)
#         return a
                
        
        
      
        
        
            
                    
        
    
        
        

            
        
        
        
        
        