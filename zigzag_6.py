class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1:
            return s

        if numRows == 1:
            return s

        ans = ["" for i in range(numRows)]
        row = 0
        i = 0
        while i < len(s):
            if row == 0:
                while row < numRows - 1 and i < len(s):
                    ans[row] += s[i]
                    row += 1
                    i += 1

            if row == numRows - 1:
                while row > 0 and i < len(s):
                    ans[row] += s[i]
                    row -= 1
                    i += 1

        return "".join(ans)
