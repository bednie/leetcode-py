from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1 
        d_int = 0 

        # convert to int
        for i,j in enumerate(digits[::-1]):
            d_int += j * 10**i
        
        # add one 
        d_int += 1 

        # convert back to list 
        d = [] 
        while d_int > 0: 
            r = d_int % 10
            d.append(r)
            d_int //= 10

        d = reversed(d)
        return d