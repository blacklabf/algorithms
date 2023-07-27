# 백준 1차원 토마토
# 시작점이 여러개일 수 있어서 visited를 해줌
# 미로탐색이랑 비교
# 시환풀이


from collections import deque


def bfs(graph, visited, startVertex):
    global cnt
    q = deque()
    
    for i,j in startVertex:
        q.append((i,j))
        visited[i][j] = True
    
    
    while q:
        
        qSize = len(q)

        while qSize != 0:
            qSize -= 1
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 1 or nx > n or ny < 1 or ny > m:
                    continue

                if visited[nx][ny] == False and graph[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    graph[nx][ny] = 1
        cnt += 1

    
global cnt
m, n = map(int, input().split())

graph = [[]]
visited = [[False] * (m+1) for i in range(n+1)]
cnt = 0

dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]

for i in range(n):
    graph.append([''] + list(map(int ,input().split())))

startVertex = []

for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i][j] == 1:
            startVertex.append((i,j))

bfs(graph, visited, startVertex)

flag = False

for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i][j] == 0:
            flag = True

if flag == True:
    print(-1)
else:
    print(cnt-1)