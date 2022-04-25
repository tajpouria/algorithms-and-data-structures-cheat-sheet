class Node:
  def __init__(self, data, next=None):
    self.data = data 
    self.next = next

  def __str__(self):
    return str(self.data)

class LinkedList:
  def __init__(self, head_data):
    head = Node(head_data, None)
    self.head = head

  @property
  def length(self):
    nxt = self.head.next
    le=1
    while nxt != None:
      le += 1
      nxt = nxt.next

    return le

  def append(self, data):
    cur = self.head
    while cur.next != None:
      cur = cur.next

    cur.next = Node(data)

  def display(self):
    els = []
    cur = self.head
    while cur.next != None:
      els.append(str(cur))
      cur = cur.next

    print('->'.join(els))

  def get(self, idx):
    l = self.length
    if idx > l - 1:
      raise Exception(f"Out of the range index: {idx}")
    cur = self.head
    for i in range(idx):
      cur = cur.next

    return cur

  def erase(self, idx):
    l = self.length
    if idx > l - 1:
      raise Exception("Out of the range index: {idx}")

    cur = self.head
    for i in range(+ 1, idx):
      cur = cur.next

    cur.next = cur.next.next
      
ll = LinkedList(2)
ll.append(3)
ll.append(4)
ll.append(3)
ll.append(1)
ll.display()
print(f"The element on the 2nd index is {ll.get(2)}")
ll.erase(2)
ll.display()
print(f"The element on the 2nd index is {ll.get(2)}")

