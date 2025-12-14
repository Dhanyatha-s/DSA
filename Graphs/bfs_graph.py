from collections import deque

def bfs(start):
  queue = deque([start])
  visisted.add(start)

  while queue:
    node = graph.popleft()
    print(node, end='')

    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.add(neighbor)
        visited.add(neighbor)
bfs("A")
