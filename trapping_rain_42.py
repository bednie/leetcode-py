from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        trap = 0
        bounds = []
        i = 1
        while i < len(height) - 1:
            l, r = None, None
            if height[i] < height[i-1]:
                l = i-1
                r = i
                while height[r] < height[l] and r < len(height)-1:
                    r += 1 
            if l != None and r != None and height[r] > height[r-1]:
                bounds.append([l,r])
                i = r
            i += 1

        i = len(height) - 2 
        while i > 0:
            r, l = None, None
            if height[i] < height[i+1]:
                r = i+1
                l = i
                while height[l] < height[r] and l > 0:
                    l -= 1 
            if l != None and r != None and height[l] > height[l+1]:
                if [l,r] not in bounds:
                    bounds.append([l,r])
                i = l
            i -= 1
            
        for i in bounds:
            area = 0
            h = min(height[i[0]], height[i[1]])
            for j in range(i[0]+1, i[1]): 
                if height[j] < h:
                    area += h - height[j]
                    height[j] = h
            trap += area 
        return trap