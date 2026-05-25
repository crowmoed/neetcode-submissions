class MinStack:

    data = []
    minn = None

    def __init__(self):
        self.data = []
        

    def push(self, val: int) -> None:
        self.data.append(val)
        if self.minn == None:
            self.minn = val
        elif val < self.minn:
            self.minn = val

    def pop(self) -> None:
        temp = self.data[-1]
        self.data = self.data[0:-1]

        if temp == self.minn:
            self.minn = float('inf')
            for i in self.data:
                if i < self.minn:
                    self.minn = i

        

    def top(self) -> int:
        
        return self.data[-1]

    def getMin(self) -> int:
        return self.minn
        
