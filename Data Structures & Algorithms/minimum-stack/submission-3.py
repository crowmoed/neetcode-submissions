class MinStack:

    data = []

    def __init__(self):
        self.data = []
        

    def push(self, val: int) -> None:
        self.data.append(val)
        

    def pop(self) -> None:
        temp = self.data[-1]
        self.data = self.data[0:-1]

        

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return min(self.data)
        
