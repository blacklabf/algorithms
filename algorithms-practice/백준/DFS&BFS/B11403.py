# 백준 11403 : 경로 찾기 (BFS)
import sys ; input = sys.stdin.readline
from collections import deque
queue = deque()

def bfs(graph, start, visited):
    queue.append(start)
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n = int(input())
graph = [] * (n+1)
for _ in range(n):
