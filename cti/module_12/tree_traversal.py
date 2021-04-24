
'''
You're given an implementation for a Node and a Tree.
Implement the level-order, pre-order, in-order and post-order traversals for these trees. Return the data of each node in a list representing the requested order.


Given a tree that looks like this:
 

tree = Tree()
tree.root = Node(9)

tree.root.left = Node(5)
tree.root.right = Node(11)

tree.root.left.left = Node(3)
tree.root.left.right = Node(7)


         9
       /   \
      5     11
    /    \
  3       7
   \     / \
     4  6   8



    9
   / \
  5   11
 / \
3   7
   / \
  6   8


    9
   / \
  5   11
 / \
3   7



        __ 9 __
       /       \
      5         11
    /    \     /   \
  3       7   10    13
   \     / \        /
     4  6   8     12


Level Order
[9,5,11,3,7]

** pseudocode v2 **

create data list
create node stack
create register of nodes with stored data
current = root

add root data to list
add node to stack

if they exist:
  add current.left.data and current.right.data to list
if left exists:
  current = current.left

add current.left.data and current.right.data to list


data_store.append(current.data)



** v1 **

if current.left:
  data_store.append(current.left.data)
if current.right:
  data_store.append(current.right.data)

if current.left:
  current = current.left
elif current.right:
  current = current.right
else:
  


In-Order
[3,5,7,9,11]

** pseudocode v1 **

  create pointer
  create data list

  create node stack
  point to head
  push head onto stack
  point to left node of head
  push node onto stack

  keep pointing to left node until next left is None
  append data to list


** pseudocode v2 **

current = root
create data list
create branch stack

# while stack:

while current.left:
  current = current.left
  add current to stack

add current.data to list

  # pop stack
  # add pop.data to list
  # current = peek
  # add current.data to list

while stack:

  if peek.right:
    current = peek.right
    add current to stack
    
    if current.left:
      while current.left:
        current = current.left
        add current to stack

      pop stack
      add pop.data to list
      current = peek
      add current.data to list

    else:
      pop stack
      add pop.data to list
      pop stack
      current = peek
      add peek.data to list

  else:


  else:
    pop stack
    add pop.data to list

  if current.left:
   current = current.left
   add current to branch stack

  
  pop branch stack
  add popped.data to data list



** pseudocode v3 **

create data list
create node stack
create register of nodes with stored data
current = root

while stack:
  if there's numbers on the left & not in register:
    move down one to the left
    add to stack
  else:
    if not in register:
      add number to list
      add node to register

    if there's a branch on the right & not in register:
      go there
      add to stack
    else:
      pop stack
      current = peek
      if not in register:
        add number to list
        add node to register

**





Pre-Order
 

[9,5,3,7,11]


Post-Order
 

[3,7,5,11,9]








'''



class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    

class Tree:
  def __init__(self):
    self.root = None
    
    
  def level_order_traversal(self):
    # return the tree as a list in a level-order sequence

    
    return []
    
    
    
  def pre_order_traversal(self):
    # return the tree as a list in a pre-order sequence (dfs)
    return []
    
  def in_order_traversal(self):
    # return the tree as a list in-order (dfs)

    # create data list
    data_store = []
    # create node stack
    node_stack = []
    # create register of nodes with stored data
    stored_register = []
    # current = root
    current = self.root
    node_stack.append(current)

    # while stack:
    while node_stack:
      # if there's numbers on the left & not in register:
      if current.left and current.left not in stored_register:
        # move down one to the left
        current = current.left
        # add to stack
        node_stack.append(current)
      # else:
      else:
        # if not in register:
        if current not in stored_register:
          # add number to list
          data_store.append(current.data)
          # add node to register
          stored_register.append(current)
    # 
        # if there's a branch on the right & not in register:
        if current.right and current.right not in stored_register:
          # go there
          current = current.right
          # add to stack
          node_stack.append(current)
        # else:
        else:
          # pop stack
          node_stack.pop()
          # current = peek
          if node_stack:
            current = node_stack[-1]
          # if not in register:
          if current not in stored_register:
            # add number to list
            data_store.append(current.data)
            # add node to register
            stored_register.append(current)


    return data_store



  def post_order_traversal(self):
    # return the tree as a list in a post-order sequence (dfs)
    
    return []


if __name__ == '__main__':

  tree = Tree()
  tree.root = Node(9)

  tree.root.left = Node(5)
  tree.root.right = Node(11)

  tree.root.left.left = Node(3)
  tree.root.left.right = Node(7)

  print(tree.in_order_traversal())


