class Node:
  def __init__(self, data):
    self.data = data
    self.next_node = None

class LinkedList:
  def __init__(self):
    self.head = None

  def add(self, data):
    # Create a new Node and stick it in the list
    node = Node(data)
    if self.head == None:
      # the list is empty
      self.head = node
    else:
      current = self.head
      while current.next_node != None:
        current = current.next_node
      current.next_node = node

  def delete(self, data):
    if self.head == None:
      return False
    current = self.head
    if current.data == data:
      # we need to delete the head
      temp_node = current.next_node
      current.next_node = None
      self.head = temp_node
    else:
      while current.next_node != None:
        previous = current
        current = current.next_node
        if current.data == data:
          temp_node = current.next_node
          previous.next_node = temp_node
          current.next_node = None
          return True
      return False
  
  def delete_at_head(self):
    if self.head == None:
      return False
    else:
      current = self.head
      data = self.head.data
      temp_node = current.next_node
      current.next_node = None
      self.head =temp_node
      return data

  def insert_before(self, n, data):
    node = Node(data)
    if n == 0:
      # insert before the head and become the new head
      temp_node = self.head
      self.head = node
      self.head.next_node = temp_node
    else:
      current = self.head
      for i in range(0,n):      
        previous = current
        current = current.next_node
        if current == None:
          previous.next_node = node
          return True
      temp_node = previous.next_node
      previous.next_node = node
      node.next_node = temp_node

  def get(self, n):
    if self.head:  
      if n == 0:
        return self.head.data
      else: 
        current = self.head.next_node
        i = 1
        while current.next_node != None and i < n:
          current = current.next_node
          i += 1
        if i == n:
          return current.data
        else:
          return None
    else:
      return None

  def delete_at(self, n):
    if self.head:  
      if n == 0:
        temp_node = self.head.next_node
        self.head.next_node = None
        self.head = temp_node
        return 
      else:
        current = self.head.next_node
        previous = self.head
        i = 1 
        while current.next_node != None and i < n:
          previous = current
          current = current.next_node
          i += 1
        if i == n:
          previous.next_node = current.next_node
          current.next_node = None
          return True
        else:
          return False
    else:
      return False

  def print_list(self):
    if self.head != None:
      current = self.head
      print(self.head.data)
      while current.next_node != None:
        current = current.next_node
        print(current.data)

class Queue:
  def __init__(self):
    self.store = LinkedList()
  
  def enqueue(self, data):
    self.store.add(data)
  
  def dequeue(self):
    data = self.store.get(0)
    self.store.delete_at(0)
    return data

class Stack:
  def __init__(self):
    self.store = LinkedList()
  
  def push(self,data):
    self.store.insert_before(0, data)
  
  def pop(self):
    data = self.store.get(0)
    self.store.delete_at(0)
    return data

s = Stack()

s.push("one")
s.push("two")
s.push("three")

print(s.pop())
print(s.pop())
print(s.pop())

q = Queue()

q.enqueue("uno")
q.enqueue("dos")
q.enqueue("tres")

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())