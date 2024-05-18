class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_length = 0 
        i = len(s) - 1 
        while i >= 0: 
            if s[i] == " ":
                i -= 1 
            else: 
                last_word_length += 1 
                if s[i-1] == " ":
                    break
                i -= 1 
            
        return last_word_length