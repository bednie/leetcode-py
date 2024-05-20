from typing import List

from collections import defaultdict 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = defaultdict(int)

        # rows
        for i in board:
            for j in i:
                if j != ".":
                    if nums[j] == 0:
                        nums[j] = 1 
                    else: 
                        return False
            nums.clear()

        # cols
        col = 0 # 0-8
        while col <= 8:
            for i in board:
                if i[col] != ".":
                    if nums[i[col]] == 0:
                        nums[i[col]] = 1 
                    else:
                        return False

            col += 1 
            nums.clear()

        # subgrids
        subgrid = [(0,0), (0,1), (0,2),
                    (1,0), (1,1), (1,2),
                    (2,0), (2,1), (2,2)]
        for s in subgrid:                
            for i in range(3):
                for j in range(3):
                    pos = board[(s[0] * 3) + i][(s[1] * 3) + j]
                    if pos != ".":
                        if nums[pos] == 0:
                            nums[pos] = 1 
                        else:
                            return False
            nums.clear()

        return True