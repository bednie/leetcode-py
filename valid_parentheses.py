# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ['(','{','[']
        closes = {'}':'{',']':'[',')':'('}
    
        if s=="" or (s[0] in [']', ')', '}']):
            return False

        for i in s:
            # push onto stack
            if i in opens:
                stack.append(i)
                
            # pop from stack
            else:
                # check if it is the expected closing char
                try:
                    if closes[i] == stack[-1]:
                        stack.pop()
                    
                    else:
                        print(closes[i],i)
                        return False
                except IndexError:
                    return False
                
        # check if stack is empty     
        if not stack:
            return True
        else:
            print(stack)
            return False