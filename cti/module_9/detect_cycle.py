
'''
Write a function that takes a Linked List and returns True if the list contains a "cycle" - eg, the list contains no node pointing to None.

For example:



Ensure your code can be called like this:

ll = LinkedList()

ll.extend([1, 2, 3, 4, 5, 6])


## now imagine if, in another file, there has been some malicious function inserted

## that creates a cycle in this linked list

cause_havoc(ll)


## thankfully, if your code works, you can detect this!

ll.has_cycle() # returns True


** repl.it unit test **

Traceback (most recent call last):
  File "/home/runner/unit_tests.py", line 93, in test_two
    self.assertEquals(ll.has_cycle(), False)
AssertionError: True != False



''''


### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than has_cycle()
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
  
  # used in test cases to create cycles in the linked list
  # if you want to test your code without submitting, consider using this function
  def get_reference(self, index):
    curr = self.head
    count = index
    while count > 0:
      curr = curr.next
      count -= 1
    return curr
      
  # implement this method
  # return true if there is a cycle in this linked list
  def has_cycle(self):
    cycle = True
    pointer = self.head
    if self.empty():
      cycle = False
      pointer = self.tail
    while pointer is not self.tail:
      if pointer == None:
        cycle = False
        pointer = self.tail
      else:
        pointer = pointer.next
    if self.tail.next == None:
      cycle = False
    return cycle

    