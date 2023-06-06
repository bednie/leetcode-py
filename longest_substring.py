# 3. Longest Substring Without Repeating Characters

# brute force
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
    
# sliding window 
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}
        left = 0
        max_len = 0

        for right,char in enumerate(s):
            if char in seen :#and left <= seen[char]:
                left = seen[char] + 1 
                seen.pop(char)

            seen[char] = right 
            max_len = max(max_len,(right-left+1)) 

        return max_len