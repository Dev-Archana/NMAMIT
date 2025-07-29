class StackArray:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def push(self, item):
        if self.is_full():
            print("Stack Overflow")
        else:
            self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def display(self):
        print("Stack:", self.stack)

# Example usage
s = StackArray(5)
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Popped:", s.pop())
s.display()
