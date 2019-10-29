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
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def append(self,data):
        node = Node(data)
        if self.head :
            self.head.next = node
            self.head = node
        else:
            self.head=node
            self.tail=node

        self.head.next = self.tail
        self.count = self.count+1

    def delete(self,data):
        current = self.tail
        prev = self.tail
        while prev == current or prev != self.head:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                    self.head.next = self.tail
                else :
                    prev.next = current.next
                self.count = self.count-1
                return
            prev = current
            current = current.next



a = circularLinkedList()
a.append("Lakshman")
a.append("Chinta")
a.append("Axelaar")
a.append("Kotesh")
counter = 1
for i in a.iter():
    print(i)
    counter = counter+1
    if counter > a.count:
        break
counter2 = 1
a.delete('Axelaar')
for i in a.iter():
    print(str(2)+i)
    counter2 = counter2 + 1
    if counter2 > a.count:
        break