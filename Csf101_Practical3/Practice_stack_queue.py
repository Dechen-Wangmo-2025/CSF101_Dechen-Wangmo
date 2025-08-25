class Stack:
    def __init__(namkha):
        namkha.items = []
    def is_empty(namkha):
        return len(namkha.items) == 0
    def push(namkha, item):
        namkha.items.append(item)
    def pop(namkha):
        if namkha.is_empty():
            return namkha.items.pop()
        else:   
            raise IndexError("The stack is Empty")
    def elements(namkha):
        return namkha.items.copy()
stack = Stack()
print(stack.pop()) 
print(stack.elements())
#since the stack is empty it will raise an error
# So we need to push some elements onto the stack using push function.
