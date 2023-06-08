# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        prefix = ""
        letter = set()
        min_len = min(len(item) for item in strs)

        for i in range(0,min_len):
            for j in strs:
                letter.add(j[i])
            if len(letter) == 1:
                prefix += letter.pop()
            else:
                break
 
        return prefix