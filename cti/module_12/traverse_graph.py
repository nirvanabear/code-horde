

'''

Given this implementation of a graph, return all of the nodes connected to a particular starting node. Return a set of the names of nodes.

For example, here's a graph:

graph = Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')
graph.add_node('Z')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('C', 'E')
graph.add_edge('E', 'F')
graph.add_edge('D', 'B')


It looks like this:

You should return:

self.subgraph('A') # ['A', 'D', 'B', 'C', 'E', 'F']







'''


class Graph:
  def __init__(self):
    self.verticies = {}


  def add_node(self,node):
    self.verticies[node] = []


  def add_edge(self,node_a,node_b):
    self.verticies[node_a].append(node_b)
    self.verticies[node_b].append(node_a)
    
  def subgraph(self, start):
    # Implement the subgraph traversal
    pass
  
graph = Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')
graph.add_node('Z')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('C', 'E')
graph.add_edge('E', 'F')
graph.add_edge('D', 'B')
