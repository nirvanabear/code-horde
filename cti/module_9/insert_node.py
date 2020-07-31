
'''
Add a method to a linked list to insert a node at the given position. Pass in two arguments, node value and insert position.

For example:

ll = LinkedList()

ll.extend([1, 2, 3, 4, 5, 6])


ll.insert(4,2)


The list would then have nodes ordered like this: 1,2,4,3,4,5,6

For the above example, it would be valid to insert an item at index 6. Inserting an item at an index equal to the list's length is the same as appending a new item to the list. Additionally, it is valid to insert an item at index 0, which puts that item at the head of the list. Make sure to account for these edge cases in your code.


** pseudocode **

new_node = LinkedNode(data)
position = index
node = self.head
for node in index - 1:
    node = self.next
new_node.next() = node.next()
node.next() = new_node


** repl.it unit test error **

Traceback (most recent call last):
  File "/home/runner/unit_tests.py", line 64, in test_head
    self.assertEquals(ll.get(0), 100)
AssertionError: 1 != 100


'''


### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than insert()
### you may insert new methods if you like
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def empty(self):
    return self.head == None
    
  def append(self, data):
    if self.empty():
      self.head = LinkedNode(data)
      self.tail = self.head
    else:
      new_node = LinkedNode(data)
      self.tail.next = new_node
      self.tail = new_node
      
  def extend(self, array):
    for element in array:
      self.append(element)
  
  # used in test cases to verify solutions
  # if you want to test your code without submitting, consider using this function
  def get(self, index):
    curr = self.head
    count = index
    while count > 0:
      curr = curr.next
      count -= 1
    return curr.data
  
  # implement this method
  def insert(self, data, index):
    if self.empty():
      self.append(data)
    elif not index:
      new_node = LinkedNode(data)
      new_node.next = self.head.next
      self.head = new_node      
    else:
      new_node = LinkedNode(data)
      node = self.head
      for element in range(index - 1):
          node = node.next
      new_node.next = node.next
      node.next = new_node


if __name__ == '__main__':

  linkedList1 = LinkedList()
  linkedList1.extend([1, 2, 3, 4, 5, 6])
  linkedList1.insert(100,0)
  print(linkedList1.get(0))


  linkedList2 = LinkedList()
  linkedList2.insert(0,100)
  print(linkedList2.get(0))
