from collections import deque

# 构建题目中的无向图邻接表
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

# DFS 递归实现
def dfs(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    visited.add(start)
    result.append(start)
    for n in graph[start]:
        if n not in visited:
            dfs(graph, n, visited, result)
    return result

# BFS 队列实现
def bfs(graph, start):
    visited = set()
    q = deque([start])
    visited.add(start)
    res = []
    while q:
        cur = q.popleft()
        res.append(cur)
        for n in graph[cur]:
            if n not in visited:
                visited.add(n)
                q.append(n)
    return res

# 输出结果
if __name__ == "__main__":
    print("DFS序列：", dfs(graph, "A"))
    print("BFS序列：", bfs(graph, "A"))