import sys

graph1 = {
  'a': {'b': 4, 'c': 8},
  'b': {'a': 4, 'd': 10, 'e': 7},
  'c': {'a': 8, 'e': 9},
  'd': {'b': 10, 'f': 3},
  'e': {'b': 7, 'c': 9, 'f': 1},
  'f': {'d': 3, 'e': 1},  
}

graph2 = {
  'a': {'b': 11, 'c': 2},
  'b': {'a': 11, 'd': 3, 'e': 4},
  'c': {'a': 2, 'e': 3},
  'd': {'b': 3, 'f': 1},
  'e': {'b': 4, 'c': 3, 'f': 12},
  'f': {'d': 1, 'e': 12},  
}

def dijkstra(graph, start, end):
  vertices = [] # hold all vertices to be processed
  distance = {} # holds updated distances to each vertex from start
  previous = {} # holds the vertex by which you came this vertex

  # initialize everything
  for key in graph:
    distance[key] = sys.maxsize # make initial distance impossibly high
    previous[key] = None
    vertices.append(key) # add all vertices to arr

  distance[start] = 0

  while len(vertices) > 0:
    # find the vertex with the current shortest distance
    min_distance = sys.maxsize
    min_key = start
    for vertex in vertices:
      if distance[vertex] < min_distance and vertex in vertices:
        min_distance = distance[vertex]
        min_key = vertex
      
    # remove vertex
    vertices.remove(min_key)

    #loop through each connected vertex and update distances
    for key in graph[min_key]:
      if key in vertices:
        new_distance = distance[min_key] + graph[min_key][key]
        if new_distance < distance[key]:
          distance[key] = new_distance
          previous[key] = min_key

  # now we can build a nice readable path to return
  path = end
  prev = previous[end]
  while prev != None:
    path = path + prev
    prev = previous[prev]

  return path[::-1]
            
print(dijkstra(graph1,'a','f'))
print(dijkstra(graph2,'a','f'))
print(dijkstra(graph2,'b','a'))
