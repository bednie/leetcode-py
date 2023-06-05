# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        longest = []
        substring = []

        for i in range(len(s)):
            next = s[i::]
            for j in range(len(next)): 
                if next[j] in substring:
                    if len(substring) >= len(longest):
                        longest = substring
                    substring = []
                    break
                else: 
                    substring.append(next[j])

        return max(len(longest),len(substring))