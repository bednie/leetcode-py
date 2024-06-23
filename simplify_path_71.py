class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        p = path.split("/")
        p = [i for i in p if i and i != "."]

        for i in p:
            if i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append("/" + i)

        if stack:
            return "".join(stack)

        return "/"
