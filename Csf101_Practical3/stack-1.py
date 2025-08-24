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
        if not dechen.is_empty(): # condition to check if the stack is empty
            return dechen.items[-2]
        else:
            raise IndexError("The Stack is empty")
    def size(dechen):
        return len(dechen.items)
    def elements(dechen): # function to return the elements in the stack
        return dechen.items.copy()
stack = stack()
stack.push(1) # Pushing elements onto the stack; giving values to the stack
stack.push(2) 
stack.push(3)
stack.push(4)
print(stack.pop())  # Calling the above functions begins from pop() to elements()
print(stack.peek())
print(stack.size())
print(stack.elements())