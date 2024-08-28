from typing import List, Optional


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(
            d: str, index: int, letters: str, result: List[str]
        ) -> Optional[List[str]]:
            if index == len(d):
                if letters:
                    result.append(letters)
                return

            for letter in self.d_to_l[d[index]]:
                letters += letter
                backtrack(d, index + 1, letters, result)
                letters = letters[:-1]

            return result

        self.d_to_l = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = backtrack(digits, 0, "", [])

        return result
