class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def float(self,k):
        while k//2 > 0:
            if self.heap[k] < self.heap[k//2]:
                self.heap[k],self.heap[k//2] = self.heap[k//2],self.heap[k]

            k = k//2

    def insert(self,item):
        self.heap.append(item)
        self.size = self.size + 1
        self.float(self.size)

    def minindex(self,k):
        if k * 2 +1 > self.size:
            return k*2
        elif self.heap[k * 2] < self.heap[k * 2 + 1]:
            return k * 2
        else:
            return k * 2 + 1

    def sink(self,k):
        while k * 2 <= self.size:
            mi = self.minindex(k)
            if self.heap[k] > self.heap[mi] :
                self.heap[k],self.heap[mi] = self.heap[mi],self.heap[k]

            k = mi

    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size = self.size - 1
        self.heap.pop()
        self.sink(1)
        return item

    def heapSort(self):
        sortedList = []
        for node in range(self.size):
            n = self.pop()
            sortedList.append(n)
        return sortedList

h = Heap()
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)
print(h.heap)
#[0, 1, 2, 5, 3, 6, 10, 7, 8, 4, 9]

print(h.heapSort())

'''for  i in range(10):
    n = h.pop()
    print(n)
    print(h.heap)


1
[0, 2, 3, 5, 4, 6, 10, 7, 8, 9]
2
[0, 3, 4, 5, 8, 6, 10, 7, 9]
3
[0, 4, 6, 5, 8, 9, 10, 7]
4
[0, 5, 6, 7, 8, 9, 10]
5
[0, 6, 8, 7, 10, 9]
6
[0, 7, 8, 9, 10]
7
[0, 8, 10, 9]
8
[0, 9, 10]
9
[0, 10]
10
[0]'''