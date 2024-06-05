class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s

        ans = ["" for i in range(numRows)]
        row, i, zigzag = 0, 0, 1
        while i < len(s):
            ans[row] += s[i]
            row += zigzag
            i += 1
            if row == numRows - 1 or row == 0:
                zigzag *= -1
        return "".join(ans)
