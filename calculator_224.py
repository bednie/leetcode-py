class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(t: list, x: int) -> int:
            while tokens:
                if tokens[0] == ")":
                    tokens.pop(0)
                    return x

                elif tokens[0] == "(":
                    tokens.pop(0)
                    x += evaluate(tokens, x)

                elif tokens[0].isdigit():
                    x += int(tokens.pop(0))

                elif tokens[0] == "-" and tokens[1].isdigit():
                    tokens.pop(0)
                    x -= int(tokens.pop(0))

                elif tokens[0] == "-" and tokens[1] == "(":
                    tokens.pop(0)
                    tokens.pop(0)
                    y = 0
                    x -= evaluate(tokens, y)

                elif tokens[0] == "+" and tokens[1].isdigit():
                    tokens.pop(0)
                    x += int(tokens.pop(0))

                elif tokens[0] == "+" and tokens[1] == "(":
                    tokens.pop(0)
                    tokens.pop(0)
                    y = 0
                    x += evaluate(tokens, y)

            else:
                return x

        tokens = []  # [i for i in s if i != " "]
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1

            elif not s[i].isdigit():
                tokens.append(s[i])
                i += 1

            else:
                if tokens and tokens[-1].isdigit():
                    tokens[-1] += s[i]
                else:
                    tokens.append(s[i])
                i += 1

        return evaluate(tokens, 0)
