class MinStack:

    def __init__(self):
        self.container = []
        self.monotonic_stack = []    

    def push(self, val: int) -> None:
        if len(self.container) == 0:
            self.container.append(val)
            self.monotonic_stack.append(val)
            return 
        self.container.append(val)
        if val <= self.monotonic_stack[-1]:
            self.monotonic_stack.append(val)
        

    def pop(self) -> None:
        val = self.container.pop()
        if self.monotonic_stack[-1] == val:
            self.monotonic_stack.pop()
        return val
        

    def top(self) -> int:
        return self.container[-1]
        
    def getMin(self) -> int:
        return self.monotonic_stack[-1]
