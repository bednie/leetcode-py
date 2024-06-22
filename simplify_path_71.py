class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = ""
        p = path.split("/")
        p = [i for i in p if i and i != '.']

        i = 0
        while i < len(p):
            if p[i] == "..":
                pass
            elif i + 1 < len(p) and p[i+1] == "..":
                i += 2
                continue
            else:
                ans += "/"
                ans += p[i]

            i += 1

        if ans:
            return ans
        
        return "/"
