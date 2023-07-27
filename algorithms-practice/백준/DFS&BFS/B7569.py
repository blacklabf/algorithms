# 백준 7569 : 토마토 2차원 (BFS)
import sys ; input = sys.stdin.readline
from collections import deque
queue = deque()

def bfs(graph,visited,startList):

    for i,j,k in startList:
        queue.append((i,j,k))
        visited[i][j][k] = True

    cnt = 0
    while queue:
        qSize = len(queue)

        for i in range(qSize):
            x, y, z = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if nx < 1 or nx > n or ny < 1 or ny > m or nz < 1 or nz > l:
                    continue
                if graph[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                    queue.append((nx,ny,nz))
                    visited[nx][ny][nz] = True
                    graph[nx][ny][nz] = 1
        cnt += 1
    return cnt
        

m, n, l = map(int, input().strip().split())
graph = [[] ] 
visited = [[False] * (m+1) for i in range(n+1) for j in range(l+1)] 

dx = [-1, 0, 0, 1, 0, 0] # 시계방향
dy = [0, 1, 0, 0, -1 ,0]
dz = [0, 0, 1, 0, 0, -1]

for j in range(1, n+1):
    graph.append([' '] + list(map(int, input().strip().split())))

startList = []
for i in range(1, n+1):
    for j in range(1, m+1):
        for k in range(1, l+1):
            if graph[i][j][k] == 1:
                startList.append((i,j,k))

ans = bfs(graph, visited, startList)

flag = False
for i in range(1,n+1):
    for j in range(1, m+1):
        for k in range(1, l+1):
            if graph[i][j][k] == 0:
                flag = True
if flag == True:
    print(-1)
else:
    print(ans-1)