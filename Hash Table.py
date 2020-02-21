class HashItem:
    def __init__(self,key,value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0

    def _hash(self,key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult = mult + 1
        return hv % self.size
    #Putting Elements
    def put(self,key,value):
        item = HashItem(key,value)
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h+1) % self.size
        if self.slots[h] is None:
            self.count = self.count + 1
        self.slots[h] = item

    #Getting  elements
    def get(self,key):
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h+1) % self.size

        return None

    #Using [] with hash table
    def __setitem__(self, key, value):
        self.put(key,value)
    def __getitem__(self, key):
        return self.get(key)

'''With out __setitem__() and __getitem__()'''
ht = HashTable()
ht.put("good", "eggs")
ht.put("better", "ham")
ht.put("best", "spam")
ht.put("ad", "do not")
ht.put("ga", "collide")

for key in ("good", "better", "best", "worst", "ad", "ga"):
    v = ht.get(key)
    print(v)

'''With __setitem__() and __getitem__()'''
#ht = HashTable()
ht["gooda"] = "eggs"
ht["bettera"] = "ham"
ht["besta"] = "spam"
ht["ada"] = "do not"
ht["gaa"] = "collide"

for key in ("gooda", "bettera", "besta", "worsta", "ada", "gaa"):
    v = ht[key]
    print(v)

print("The number of elements is: {}".format(ht.count))

'''Hash table load factor:
The hash table's load factor gives us an indication of how large a portion of the available slots are being used. It is defined as follows:
load factor = n/k
where n is number of used slots
k is the total number of slots'''