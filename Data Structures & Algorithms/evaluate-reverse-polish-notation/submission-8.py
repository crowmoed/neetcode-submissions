class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        stack = []


        for i in (tokens):
            
            
            
            if i == "+":
                stack.append(stack[-2]+stack[-1])
                stack = stack[0:-3] + stack[-1::]
            
            elif i == "-":
                stack.append(stack[-2]-stack[-1])
                stack = stack[0:-3] + stack[-1::]
            
            elif i == "*":
                
                stack.append(stack[-2] * stack[-1])
                stack = stack[0:-3] + stack[-1::]
            
            elif i == "/":
                stack.append(int(stack[-2] / stack[-1]))
                stack = stack[0:-3] + stack[-1::]
            else:
                stack.append(int(i))
            
            print(stack)
        return stack[0]