from collections import defaultdict
from typing import List


class Solution:
    """from tamimlikhon456: https://leetcode.com/problems/substring-with-concatenation-of-all-words/solutions/5236702/beats-97-68-of-users-with-python3-61ms"""
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) < len(words[0]) * len(words) or not s or not words:
            return []

        ans = []
        word_length = len(words[0])
        word_map = defaultdict(int)
        for word in words:
            word_map[word] += 1

        for i in range(word_length):
            l, r = i, i
            checked = defaultdict(int)
            count = 0 

            while r + word_length <= len(s):
                r_word =  s[r : r + word_length]
                r += word_length

                if r_word in word_map:
                    # add
                    checked[r_word] += 1
                    count += 1 

                    # drop
                    while checked[r_word] > word_map[r_word]:
                        l_word = s[l : l + word_length]
                        checked[l_word] -= 1
                        count -= 1 
                        l += word_length
                        
                    # compare
                    if count == len(words):
                        ans.append(l)
                    
                else:
                    checked.clear()
                    count = 0
                    l = r 

        return ans
