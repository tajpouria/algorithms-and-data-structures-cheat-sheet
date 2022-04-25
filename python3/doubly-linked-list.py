class Node:
  def __init__(self, data, prv=None, nxt=None):
    self.data = data
    self.prv = prv
    self.nxt = nxt

  def __str__(self):
    return str(self.data)


class DoublyLinkedlist:
  def __init__(self, init_data):
    n = Node(init_data)
    self.head = n
    self.tail = n

  def __str__(self):
    cur = self.head
    els = [str(cur)]
    while cur.nxt != None:
      cur = cur.nxt
      els.append(str(cur))

    return '<->'.join(els)

  @property
  def length(self):
    cur = self.tail
    l = 1
    while cur.prv != None:
      cur = cur.prv
      l += 1

    return l

  def push(self, data):
    n = Node(data, prv=self.tail)
    self.tail.nxt = n 
    self.tail = n

  def unshift(self, data):
    n = Node(data, nxt=self.head)
    self.head.prv = n
    self.head = n


dll = DoublyLinkedlist(1)
dll.push(2)
dll.push(3)
dll.push(4)
dll.unshift(0)
print(dll.length)
print(dll)

