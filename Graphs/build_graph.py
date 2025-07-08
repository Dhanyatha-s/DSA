def build_graph(edges):
  graph = {}
  for u,v in edges:
    graph.setdefault(u,[]).append(v)
    graph.setdefault(v,[]).append(u)

  return graph

graph = build_graph(edges)
print(graph)


edges = [(0,1), (0,3), (1,2), (2,4), (4,5)
