from collections import deque
class Graph:
    def __init__(self):
        self.adj_list = {}
    def add_edge(self, src, dest):
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dest not in self.adj_list:
            self.adj_list[dest] = []
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result
    def dfs_recursive(self, start):
        visited = set()
        result = []
        def dfs(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.adj_list.get(node, []):
                    dfs(neighbor)
        dfs(start)
        return result
    def dfs_iterative(self, start):
        visited = set()
        stack = [start]
        result = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in reversed(self.adj_list.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result
g = Graph()
for src, dest in [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F')]:
    g.add_edge(src, dest)
print("BFS from A:", g.bfs('A'))
print("DFS Recursive from A:", g.dfs_recursive('A'))
print("DFS Iterative from A:", g.dfs_iterative('A'))