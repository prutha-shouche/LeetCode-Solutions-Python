# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1678. Goal Parser Interpretation

class Solution:
    def interpret(self, command: str) -> str:
        s=""
        for i in range(len(command)):
            if command[i]=='G':
                s=s+"G"
            elif command[i]=='(' and command[i+1]==')':
                s=s+"o"
            else:
                if command[i]=='(' and command[i+1]=='a':
                    s=s+"al"
        return s
                
        
                
                
        
            
                    
        
    
        
        

            
        
        
        
        
        