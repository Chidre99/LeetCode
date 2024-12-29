class MinStack:

    def __init__(self):
        self.stack = []       # Main stack to store elements
        self.min_stack = []   # Auxiliary stack to track minimums

    def push(self, x: int) -> None:
        # Push the element onto the main stack
        self.stack.append(x)
        
        # Push onto the min_stack the new minimum
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            # If the popped element is the current minimum, pop from min_stack
            if popped == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None  # Return None if the stack is empty

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None  # Return None if the stack is empty
