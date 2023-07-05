class MinStack:
    def __init__(self):
        self.stack = []
        self.minvals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minvals:
          val = min(val, self.minvals[-1]) 
        self.minvals.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minvals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minvals[-1]

mins = MinStack()
mins.push(-2)
mins.push(0)
mins.push(-3)
mins.getMin()
mins.pop()
mins.top()
mins.getMin()

