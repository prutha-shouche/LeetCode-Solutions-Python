# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 657. Robot Return to Origin

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        #U -> increase in y axis
        #R -> increase in x axis
        #D -> decrease in y axis
        #L -> decrease in x axis
        
        x=0
        y=0
        for move in moves:
            if move=='U':
                y+=1
            elif move=='D':
                y-=1
            elif move=='R':
                x+=1
            elif move=='L':
                x-=1
        if x==0 and y==0:
            return True
        return False
        