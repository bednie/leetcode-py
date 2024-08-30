from typing import List, Optional


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(
            c: List[int],
            candidate_sum: int,
            freq: dict,
        ) -> Optional[List[List[int]]]:
            if candidate_sum == target and str(freq) not in frequencies:
                result.append(c[:])
                frequencies.add(str(freq))
            
                return

            for num in candidates:
                if candidate_sum + num <= target:
                    c.append(num)
                    freq[num] += 1
                    backtrack(c, candidate_sum + num, freq)
                    c.pop()
                    freq[num] -= 1

            return result

        result = []
        freq = {num: 0 for num in candidates}
        frequencies = set()  

        return backtrack([], 0, freq)
