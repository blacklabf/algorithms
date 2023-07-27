# 백준 1952 : 달팽이2
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
graph = [[0]* m for _ in range(n)] # n, m 조심하기
cnt = 0
dx = [0, 1 , 0 , -1]
dy = [1, 0 ,-1, 0]

x, y = 0, 0
move = 0

for i in range(1, n*m+1):
    graph[x][y] = i
    x += dx[move]
    y += dy[move]
    if x < 0 or y < 0 or x >= n or y >= m or graph[x][y] != 0:
        cnt += 1
        x -= dx[move]
        y -= dy[move]
        move = (move+1) % 4
        x += dx[move]
        y += dy[move]
print(cnt-1)