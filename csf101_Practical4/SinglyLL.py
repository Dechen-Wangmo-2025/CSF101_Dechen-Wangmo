class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current= current.next
        print("->".join(map(str, elements)))
        
ll = SinglyLinkedList()
ll.insert(10)
ll.insert(20)   
ll.insert(30)
ll.display()

print()

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
        for d in range(position - 1):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        print("->".join(map(str, elements)))

ll = LinkedList()
ll.insert(10,1)
ll.display()