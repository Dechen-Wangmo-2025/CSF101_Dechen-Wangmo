class Queue:
    def __init__(dekday):
        dekday.items = []
    def is_empty(dekday):
        return len(dekday.items) == 0
    def enqueue(dekday, item):
        dekday.items.append(item)
    def elements(dekday):
        return dekday.items()
    def dequeue(dekday):
        if not dekday.is_empty():
            return dekday.items.pop(0)
        else:
            raise IndexError("The Queue is empty")
    def front(dekday):
        if not dekday.is_empty():
            return dekday.items[1]
        else:
            raise IndexError("The Queue is empty")
    def front(dekday):
        if not dekday.is_empty():
            return dekday.items.pop(1)
        else:
            raise IndexError("The Queue is empty")
    def size(dekday):
        return len(dekday.items)
    def elements(dekday):
        return dekday.items.copy()
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.elements())
print(queue.dequeue())
print(queue.front())
print(queue.size())
print(queue.elements())