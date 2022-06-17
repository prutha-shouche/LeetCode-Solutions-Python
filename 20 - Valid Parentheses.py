# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 20. Valid Parentheses


class Solution:
    def isEqual(self, ch1,ch2)-> bool:
        if (ch1=='(' and ch2==')'):
            return True
        if (ch1=='{' and ch2=='}'):
            return True
        if (ch1=='[' and ch2==']'):
            return True
        return False
    def isValid(self, s: str) -> bool:
        st=[]
        for ch in s:
            if len(st)!=0:
                a = st[-1]
                if self.isEqual(a,ch):
                    st.pop()
                    continue
            st.append(ch)
        return len(st)==0
        
      
        
        
            
                    
        
    
        
        

            
        
        
        
        
        