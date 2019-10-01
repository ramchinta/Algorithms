class Node(object):
    def __init__(self,data=None,next= None,prev = None):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList(object) :
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def iter(self):
        current = self.head
        while current :
            val = current.data
            current = current.next
            yield val

    def append(self,data):
        new_node = Node(data,None,None)
        if self.head is None :
            self.head = new_node
            self.tail = self.head
            self.count = self.count+1

        else :
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.count = self.count+1


    def delete(self,data):
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted =True
        elif self.tail.data == data :
            self.tail = self.tail.perv
            self.tail.next = None
            node_deleted =True
        else :
            while current:
                if current.data ==data:
                    current.prev.next =current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

        if node_deleted == True:
            self.count = self.count - 1


    def search(self,data):
        for i in self.iter():
            if  data == i:
                return True
        return False


a = doublyLinkedList()
a.append("Lakshman")
a.append("Chinta")
a.append("Axelaar")
a.append("Kotesh")
for i in a.iter():
    print(i)
a.delete('Axelaar')
for i in a.iter():
    print(str(2)+i)
print(a.search('Lakshman'))
print(a.search('Kotesh'))
print(a.search('California'))





