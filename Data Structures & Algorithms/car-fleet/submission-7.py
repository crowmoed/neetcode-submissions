class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for index,pos in enumerate(position):
            stack.append([pos, speed[index]])

        stack.sort(key = lambda x : x[0], reverse=True)
        
        retval = 0
        print(stack)

        for index,car in enumerate(stack):
            stack[index] = (target-car[0])/car[1]
        print(stack)

        x = stack[0]
        retval += 1
                
        while len(stack)>0:

                    
            if stack[0]<= x:
                pass
            else:
                retval+=1
                
            if x < stack[0]:
                x = stack[0]

            stack = stack[1::]

            
            


        return retval