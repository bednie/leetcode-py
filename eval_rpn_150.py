from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())

            elif i == '*':
                stack.append(stack.pop() * stack.pop())

            elif i == '-':
                arg1 = stack.pop()
                arg2 = stack.pop()
                stack.append(arg2 - arg1)

            elif i == '/':
                arg1 = stack.pop()
                arg2 = stack.pop()
                stack.append(int(arg2 / arg1))

            else:
                stack.append(int(i))

            print(stack)

        
        return stack.pop()
    