class stack:
    def __init__(dechen):
        dechen.items = []
    def is_empty(dechen):
        return len(dechen.items) == 0
    def push(dechen, item):
        dechen.items.append(item)

    def pop(dechen):
        if not dechen.is_empty():
            return dechen.items.pop()
        else:
            raise IndexError("The Stack is empty")
    def peek(dechen):
        if not dechen.is_empty():
            return dechen.items[-2]
        else:
            raise IndexError("The Stack is empty")
    def size(dechen):
        return len(dechen.items)
stack = stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  
print(stack.peek())
print(stack.size())