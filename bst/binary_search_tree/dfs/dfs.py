# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# Exercise on BFS, and DFS, code are from the website above

from collections import deque

def dfs(graph, start):
    # visited is the set of visited vertices
    # stack is the vertices to be visit
    # To start, add the source vertex to the list
    visited, stack = set(), [start]
    while stack:
        # the next vertex to be visited
        vertex = stack.pop()
        # check if visited
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def dfs2(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    # get the difference
    #tmp = [x for x in graph[start] if x not in visited]
    #for next in tmp:
    for next in graph[start] - visited:
        dfs2(graph, next, visited)
    return visited


def dfs_path(graph, start, goal):
    # avoid O(n) with regular list
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            # next is the vertex in the unvisited path
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def dfs_path2(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        return path
    for next in graph[start] - set(path):
        return dfs_path2(graph, next, goal, path+[next])

def bfs_path(graph, start, goal):
    # avoid O(n) with regular list
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in graph[vertex] - set(path):
            # next is the vertex in the unvisited path
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def bfs_path2(graph, start, goal):
    try:
        return next(bfs_path(graph, start, goal))
    except StopIteration:
        return None

if __name__ == '__main__':
    G = {'A': set(['B','C']),
     'B': set(['A','D','E']),
     'C': set(['A','F']),
     'D': set(['B']),
     'E': set(['B', 'F']),
     'F': set(['C', 'E'])}
  #   G = {'A': ['B','C'],
  #    'B': ['A','D','E'],
  #    'C': ['A','B'],
  #    'D': ['B'],
  #    'E': ['B', 'F'],
  #    'F': ['C', 'E']}
    #print dfs(G, 'A')
    #print result
    #print dfs2(G, 'C')
    #print list(dfs_path(G, 'C', 'F'))
    #print list(dfs_path2(G, 'A', 'F'))
    print bfs_path2(G, 'A', 'F')