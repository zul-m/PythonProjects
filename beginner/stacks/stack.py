class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        l = len(self.items) - 1
        return self.items[1]
    def size(self):
        return len(self.items)

# Now let’s add some items into the stacks and initialize some of the functions of a stack using Python.
stack = Stack()
print(stack.is_empty())

for i in range(0, 10):
    stack.push(i)

print(stack.size())
print(stack.items)