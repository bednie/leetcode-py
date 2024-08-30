from typing import List, Optional


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(
            c: List[int],
            candidate_sum: int,
            target: int,
            freq: dict,
            frequencies: set,
            result: List[List[int]],
        ) -> Optional[List[List[int]]]:
            if candidate_sum == target and str(freq) not in frequencies:
                r = []
                for k in freq:
                    for v in range(freq[k]):
                        r.append(k)

                result.append(r)
                frequencies.add(str(freq))
                
                return

            for num in c:
                if candidate_sum + num <= target:
                    freq[num] += 1
                    backtrack(c, candidate_sum + num, target, freq, frequencies, result)
                    freq[num] -= 1

            return result

        result = []
        freq = {num: 0 for num in candidates}
        frequencies = set()  

        return backtrack(candidates, 0, target, freq, frequencies, result)
