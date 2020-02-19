class Node:
  def __init__(self,data):
    self.data=data
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

    self.count = self.count+1

  def pop(self):
    if self.top:
      data=self.top.data
      self.count = self.count - 1
      if self.top.next:
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



class TreeNode :
  def __init__(self,data):
    self.data = data
    self.left  = None
    self.right = None


  def calc(node):
    if node.data == '+':
        return TreeNode.calc(node.left) + TreeNode.calc(node.right)
    elif node.data == '-' :
        return TreeNode.calc(node.left) - TreeNode.calc(node.right)
    elif node.data is '*':
        return TreeNode.calc(node.left) * TreeNode.calc(node.right)
    elif node.data is '/':
        return TreeNode.calc(node.left)/TreeNode.calc(node.right)
    else:
        return node.data



expr = '4 5 + 5 3 + *'.split()
stack = Stack()
for term in expr :
  if term in '+-*/' :
    node = TreeNode(term)
    node.right = stack.pop()
    node.left = stack.pop()
  else :
    node = TreeNode(int(term))
  stack.push(node)

root = stack.pop()
result = TreeNode.calc(root)
print(result)