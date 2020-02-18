class Node:
    def __init__(self,data,next =None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enque(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count = self.count+1

    def deque(self):
        current = self.head.data
        if self.count == 1:
            self.head = None
            self.tail = None
            self.count = self.count -1
            return current
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
            self.count = self.count -1
            return current
        else:
            return None

#Queue Application:

from random import randint

class Track:
    def __init__(self,title = None):
        self.title = title
        self.length = randint(5,10)

import time

class mediaPlayerQueue(queue):
    def __init__(self):
        super(mediaPlayerQueue,self).__init__()

    def addTrack(self,track):
        self.enque(track)

    def play(self):
        while self.count > 0:
            currentTrackNode = self.deque()
            print ('Now Playing {'+currentTrackNode.title + '}')
            time.sleep(currentTrackNode.length)

track1 = Track('Song 1')
track2 = Track('Song 2')
track3 = Track('Song 3')
track4 = Track('Song 4')
track5 = Track('Song 5')
track6 = Track('Song 6')

a = mediaPlayerQueue()
a.addTrack(track1)
a.addTrack(track2)
a.addTrack(track3)
a.addTrack(track4)
a.addTrack(track5)
a.addTrack(track6)
a.play()