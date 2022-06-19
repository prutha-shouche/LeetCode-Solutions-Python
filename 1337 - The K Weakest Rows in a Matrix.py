# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1337. The K Weakest Rows in a Matrix

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        #Approach 1
        temp=[]
        for i,m in enumerate(mat):
            sol=(sum(m),i) #since it has only 1 and 0, the total sum will be total 1s.
            temp.append(sol)
        temp.sort()
        idx=[]
        for i in range(k):
            idx.append(temp[i][1])
        return idx
        
        #Approach-2
        # row=len(mat)
        # col=len(mat[0])
        # arr=[]
        # for i, r in enumerate(mat):
        #     c=0
        #     for j in range(col):
        #         if r[j]==0:
        #             break
        #         c=c+1
        #     arr.append((c,i))
        # arr.sort()
        # index=[]
        # for i in range(k):
        #     index.append(arr[i][1])
        # return index

                
                
                
        
        
            
        
            
        
        
        

            
        
        
        
        
        