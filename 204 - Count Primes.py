# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 204. Count Primes

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        #initializing all elements of array of size n as Prime
        isPrime=[True]*n  #all elements from 2 to n will be prime 
        isPrime[0]=isPrime[1]=False  #except 0 and 1
        sqrtn=int(math.ceil(math.sqrt(n)))
        for i in range(0,sqrtn):
            if (isPrime[i]):
                #multiples of i will be non-prime. convert them.
                for multiples_of_i in range(i*i,n,i):
                    isPrime[multiples_of_i]=False
        return sum(isPrime) #return no of prime elements in the array
        
        