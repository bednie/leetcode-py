class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(" ")
        s = " ".join(s).split()

        return " ".join(reversed(s))