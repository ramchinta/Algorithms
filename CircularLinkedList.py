class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circularLinkedList :
    def __init__(self):
        self.head=None
        self.tail=None
        self.count = 0

    def iter(self):
        current = current.tail
        while current:
            val = current.data
            current = current.next
            yield val