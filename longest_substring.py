# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = ""
        substring = ""

        for char in s:            
            if char in substring:
                if len(substring) >= len(longest):
                    longest = substring
                substring = char

            else: 
                substring += char
            
        return len(longest)