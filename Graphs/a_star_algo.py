import heapq

def heuristic(a,b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
  open_set = []
  heapq.heappush(open_set, (0,start))

  came_from = {}
  g_score = {start:0}

  while open_set:
    _,current = heapq.heappop(open_set)

    if current == goal:
      path = []

      while current in came_from:
        path.append(current)
        current = came_from[current]
  
       path.append(start)
       return path[::-1]

  x,y = current
  for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
    neighbor = x+dx , y+dy   # cuurent tile we are in

    if 0 <= neighbor[0] <= len(grid) and  0<= neighbor[1] <= len(grid[0]):  # are we (the tile we've choosen) inside of the geid
 
      if grid[neighbor[0]][neighbor[1]] == 1:  # if its a wall
        continue

      g = g_score[current] + 1

      if neighbor not in g_score or g < g_score[neighbor]: # if this tile's neighbor is not in total tracked cost or if we've found the new best lowest cost amongest to it 
        # we will have that as a new lowest cost
         g_score[neighbor] = g   # updated cost 
        
         f = g + heuristic(neigbor, goal)

         heapq.heappush(open_set, {f, neighbor)

         came_from[neighbor] = current
return None


grid = [
  [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
]

start = (0,0)
goal = (4,4)

path = a_star(grid, start, goal)

if path:
  print("Path Found")
  for steps in path:
    print(steps)

else:
    print("No path found.")
    
  
# Corrected Intendations 
# import heapq

# def heuristic(a, b):
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

# def a_star(grid, start, goal):
#     open_set = []
#     heapq.heappush(open_set, (0, start))

#     came_from = {}
#     g_score = {start: 0}

#     while open_set:
#         _, current = heapq.heappop(open_set)

#         if current == goal:
#             path = []
#             while current in came_from:
#                 path.append(current)
#                 current = came_from[current]
#             path.append(start)
#             return path[::-1]

#         x, y = current
#         for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
#             neighbor = (x + dx, y + dy)

#             # Corrected boundary check
#             if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
#                 if grid[neighbor[0]][neighbor[1]] == 1:
#                     continue

#                 g = g_score[current] + 1

#                 if neighbor not in g_score or g < g_score[neighbor]:
#                     g_score[neighbor] = g
#                     f = g + heuristic(neighbor, goal)

#                     # Use tuple, not set!
#                     heapq.heappush(open_set, (f, neighbor))

#                     came_from[neighbor] = current

#     return None  # only return None after the while loop finishes

# # Test grid
# grid = [
#     [0, 0, 0, 0, 0],
#     [1, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0],
#     [0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0],
# ]

# start = (0, 0)
# goal = (4, 4)

# path = a_star(grid, start, goal)

# if path:
#     print("Path Found:")
#     for step in path:
#         print(step)
# else:
#     print("No path found.")

    
