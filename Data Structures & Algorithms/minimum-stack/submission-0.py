class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:

        # If stack is empty
        if not self.stack:
            min_so_far = val

        # If stack already has elements
        else:
            current_min = self.stack[-1][1]
            min_so_far = min(val, current_min)

        # Store (value, minimum_so_far)
        self.stack.append((val, min_so_far))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]