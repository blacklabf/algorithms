# SWEA 1954 : 달팽이 숫자
import sys ; input = sys.stdin.readline
# 오 , 아 , 왼 , 위
# 방향전환 : 방문처리 -> 1로 바꿔준 다음에 1이 되면 멈춰/ idx를 넘어가도 멈춰?
dx = [0 , 1 , 0, -1]
dy = [1, 0, -1, 0]

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]
    x, y = 0, 0
    move = 0

    for i in range(1, n*n+1):
        snail[x][y] = i
        x += dx[move]
        y += dy[move]
        if x < 0 or y < 0 or x >= n or y >= n or snail[x][y] !=0 :
            x -= dx[move]
            y -= dy[move]
            move = (move+1) % 4
            x += dx[move]
            y += dy[move]

    print("#{}".format(t))
    for row in snail:
        print(*row, end='\n')


# sol2 : while & 방향벡터
# DFS 랑 방향벡터

