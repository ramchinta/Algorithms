class Node :
    def __init__(self,data = None):
        self.data = data
        self.next = None

class SinglyLinkedList :
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def iter(self):
        current = self.tail
        while current :
            val = current.data
            current = current.next
            yield val

    def append(self,data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
            self.size = self.size+1
        else:
            self.head = node
            self.tail = node
            self.size = self.size+1

    def delete(self,data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail :
                    self.tail = current.next
                else:
                    prev.next = current.next
                    return

                self.size = self.size - 1
            else :
                prev = current
                current = current.next

    def search(self,data):
        for i in self.iter():
            if data == i:
                return True
        return False

    def clear(self):
        self.head = None
        self.tail = None


a = SinglyLinkedList()
a.append('Lakshman')
a.append('Chinta')
a.append("IBM")
a.append("Kotesh")
for i in a.iter():
    print(i)
a.delete('IBM')
for i in a.iter():
    print(str(2)+i)
print(a.search('Chinta'))
print(a.search('Virginia'))
a.clear()
for i in a.iter():
    print(i)