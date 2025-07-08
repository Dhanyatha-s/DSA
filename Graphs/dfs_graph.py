from collections import defaultdict
# defaultdict , add neighbours even if its not yet added

graph = defaultdict(list)

def add_edge(u,v):
  graph[u].append(v)
  graph[v].append(u)   # neighbours

# Add all the connections
add_edge('A', 'B')
add_edge('A', 'C')
add_edge('B', 'D')
add_edge('C', 'E')

# DFS
visited = ()  # set
def dfs(node):
 
  if node not n visited:
    print(node, end='')
    visited.add(node)

    for neighbor in graph[node]:
      dfs(neighbor)

dfs('A')



