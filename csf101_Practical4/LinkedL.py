class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        for a in range(position - 2):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next
            new_node.next = current.next
            current.next = new_node

    def display(self):
        elements = [1,2,3,4]
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        print("->".join(map(str, elements)))

ll = LinkedList()
# Insert 3 at position 1
ll.display()