# 백준 10026번 : 적록색약
from collections import deque
import sys; input = sys.stdin.readline

n= int(input())
graph = [[]]
visited = [[False] * (n+1) for _ in range(n+1)]


for i in range(1, n+1):
    graph[i].append(input().strip())


def bfs(graph,visited,startVertex):
    

