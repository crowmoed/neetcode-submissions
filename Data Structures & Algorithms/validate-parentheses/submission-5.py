class Solution:
    def isValid(self, s: str) -> bool:
        slibrary= {
            '(':')',
            '{':'}',
            '[':']',
        }
        r_slibrary = {
            ')':'(',
            ']':'[',
            '}':'{',

        }
        stack = []

        for i in s:
            if i in slibrary:
                stack.append(i)
            
            if i in r_slibrary:
                if (len(stack)== 0 ):
                    return False
                if stack[-1] == r_slibrary[i]:
                    stack.pop()
                else:
                    return False


        return len(stack) == 0
        
        
