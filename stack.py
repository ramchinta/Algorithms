class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self,data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.count = self.count + 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.count =self.count - 1
            if self.top.next :
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

def checkbrackets(statement):
    stack = Stack()
    for i in statement:
        if i in ('{', '[', '('):
            stack.push(i)
        if i in ('}', ']', ')'):
            last = stack.pop()
            if last == '{' and i == '}':
                continue
            elif last == '[' and i == ']':
                continue
            elif last == '(' and i == ')':
                continue
            else:
                return False

    if stack.count > 0:
        return False
    else:
        return True

print(checkbrackets('La[Ks]Hm{a{N}}(Chinta)'))
print(checkbrackets('C[H}in[]ta()'))