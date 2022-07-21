

'''

Imagine if you were building a social network from scratch! A private social network for your school. You know that all of the students are in clubs and things that generally create communities already, but that sometimes those communities don't share all the contact information. You want to build a friendship-suggester, so that people who are already in the same social circles can become friends.

You have a social graph already for tracking friendships. Here's an example graph:

 

graph = SocialGraph()

## Friend Group 1
graph.add_node('Alice')
graph.add_node('Bob')
graph.add_node('Carol')
graph.add_node('Dave')
graph.add_node('Eve')
graph.add_node('Faythe')
graph.add_node('Grace')

## Friend Group 2
graph.add_node('Zed')
graph.add_node('Xavier')
graph.add_node('Quill')
graph.add_node('Robert')


## Friend Group 3
graph.add_node('Heidi')
graph.add_node('Niaj')
graph.add_node('Ivan')
graph.add_node('Trent')


## Friendships
graph.add_edge('Alice', 'Bob')
graph.add_edge('Alice', 'Carol')
graph.add_edge('Alice', 'Dave')
graph.add_edge('Bob', 'Dave')
graph.add_edge('Carol', 'Dave')
graph.add_edge('Alice', 'Eve')
graph.add_edge('Eve', 'Grace')
graph.add_edge('Eve', 'Bob')
graph.add_edge('Faythe', 'Eve')
graph.add_edge('Dave', 'Faythe')
graph.add_edge('Grace', 'Faythe')


graph.add_edge('Xavier', 'Quill')
graph.add_edge('Robert', 'Quill')
graph.add_edge('Xavier', 'Robert')
graph.add_edge('Zed', 'Quill')
graph.add_edge('Zed', 'Xavier')

graph.add_edge('Heidi', 'Niaj')
graph.add_edge('Heidi', 'Ivan')
graph.add_edge('Heidi', 'Trent')
graph.add_edge('Niaj', 'Trent')
graph.add_edge('Ivan', 'Trent')
graph.add_edge('Niaj', 'Ivan')



Here's that graph, visualized:

There are three cliques- but not everyone in the groups are already friends.

Create a method for your graph called suggest_friends that takes in a user's name, and suggests friends for them based on who is friends with people they are already friends with.
Return a set that suggests all the friends with the highest count of common friendships:

graph.suggest_friends('Faythe') # {'Alice', 'Bob'}
graph.suggest_friends('Robert') # {'Zed'}
graph.suggest_friends('Ivan') # set()






'''

class SocialGraph:
  def __init__(self):
    self.members = {}


  def add_node(self,node):
    self.members[node] = set()


  def add_edge(self,node_a,node_b):
    self.members[node_a].add(node_b)
    self.members[node_b].add(node_a)
    
  def subgraph(self, root):
    to_visit = [root]

    visited = set()

    while len(to_visit) > 0:
      node = to_visit.pop(0)
      if node not in visited:
        
        visited.add(node)

        for neighbor in self.members[node]:
          to_visit.append(neighbor)
    return visited
    
  def suggest_friends(self, me):
    pass
