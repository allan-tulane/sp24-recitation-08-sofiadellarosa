from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    def shortest_helper(visited, frontier, edge):
      if len(frontier) == 0:
          return visited
      else: 
        # Pick next closest node from heap
        distance, edge, node = heappop(frontier)
        if node in visited:
          # Already visited, so ignore this longer path
          return shortest_helper(visited, frontier, edge + 1)
        else: 
          # We now know the shortest path from source to node.
          # insert into visited dict.
          visited[node] = (distance, edge)
          print('visiting: ', node, 'with distance: ', distance, 'with edge',
                edge)
          # Visit each neighbor of node and insert into heap.
          # We may add same node more than once, heap
          # will keep shortest distance prioritized.
          for neighbor, weight in graph[node]: 
            heappush(frontier, (distance + weight, edge + 1, neighbor))

          return shortest_helper(visited, frontier, edge + 1)
    visited = dict()
    frontier = []
    heappush(frontier, (0, 0, source))
    return shortest_helper(visited, frontier, 0)
        
    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    
    def bfs_helper(visited, frontier, parent):
      while frontier: 
        curr = frontier.pop() # get last element of frontier
        visited.add(curr)
        for neighbor in graph[curr]:
          if neighbor not in parent:
            parent[neighbor] = curr
          if neighbor not in visited:
            frontier.append(neighbor)
      return parent

    # initialize visited, frontier, and parent
    visited = set()
    frontier = deque()
    parent = {}
    frontier.append(source)
    return bfs_helper(visited, frontier, parent)
    


def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []
    while destination in parents: 
      destination = parents[destination]
      path = [destination] + path # prepend 
    return ''.join(path) # convert list to string 


#test_get_path()
graph = get_sample_graph()
parents = bfs_path(graph, 's')
p = get_path(parents, 'd')
print(p)

